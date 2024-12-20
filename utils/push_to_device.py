#!/usr/bin/env python3
# takes an argument of the project folder name and copies everything from there onto the ESP32 
# (except for files listed in .mpignore)

import os
import sys
import re
import subprocess

def fnmatch_to_regex(pattern):
    pattern = pattern.strip()
    pattern = pattern.replace(".", r"\.").replace("*", ".*").replace("?", ".")
    return f"^{pattern}$"

def load_ignore_patterns(ignore_file_path):
    patterns = []
    if os.path.exists(ignore_file_path):
        with open(ignore_file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    patterns.append(re.compile(fnmatch_to_regex(line)))
    return patterns

def should_ignore(rel_path, ignore_patterns):
    for pattern in ignore_patterns:
        if pattern.match(rel_path):
            return True
    return False

def ensure_remote_dir(path):
    if not path or path == "/":
        return
    parts = path.strip("/").split("/")
    cur = ""
    for p in parts:
        cur = f"{cur}/{p}"
        subprocess.run(["mpremote", "fs", "mkdir", f":{cur}"], capture_output=True)

def upload_files(local_dir, remote_dir, ignore_patterns):
    for root, dirs, files in os.walk(local_dir, topdown=True):
        # Compute the relative path to local_dir
        rel_dir_path = os.path.relpath(root, local_dir)
        if rel_dir_path == ".":
            rel_dir_path = ""

        # Filter out ignored directories before descending into them
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(rel_dir_path, d), ignore_patterns)]

        # Ensure directory on device if not root
        remote_subdir = (f"{remote_dir}/{rel_dir_path}").rstrip("/")
        if remote_subdir and remote_subdir != "/":
            ensure_remote_dir(remote_subdir.lstrip("/"))

        # Upload files that are not ignored
        for filename in files:
            rel_file_path = os.path.join(rel_dir_path, filename)
            if should_ignore(rel_file_path, ignore_patterns):
                continue
            local_file_path = os.path.join(root, filename)
            remote_file_path = f"{remote_subdir}/{filename}".lstrip("/")
            subprocess.run(["mpremote", "fs", "cp", local_file_path, f":/{remote_file_path}"])

def main():
    if len(sys.argv) != 2:
        print("Usage: python push_to_device.py <directory_name>")
        sys.exit(1)

    base_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    local_dir = os.path.join(base_dir, sys.argv[1])
    if not os.path.exists(local_dir):
        print(f"Error: Directory '{local_dir}' does not exist.")
        sys.exit(1)

    ignore_file_path = os.path.join(local_dir, ".mpignore")
    ignore_patterns = load_ignore_patterns(ignore_file_path)

    upload_files(local_dir, "/", ignore_patterns)

if __name__ == "__main__":
    main()
