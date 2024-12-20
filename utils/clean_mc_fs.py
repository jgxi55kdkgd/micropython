# mpremote run clean_mc_fs.py
# removes everything from the MC **EXCEPT** exclude lists below. 
# can't pass options into an "mpremote run" command so it requires some script duplication.

import os

# Exclusion lists
EXCLUDED_FILES = ["secrets.py"]  # Add filenames to exclude
EXCLUDED_DIRECTORIES = ["lib"]  # Add directory names to exclude

DIRECTORY_MARKER = 32768
FILE_MARKER = 16384

def notify(*args: str) -> None:
    print(*args)  # noqa: T201


def join(path_a: str, path_b: str) -> str:
    return f"{path_a}/{path_b}"


def list_files(base: str) -> list:
    # micropython: -> ignore attr-defined
    return [d[0] for d in os.ilistdir(base) if d[1] == FILE_MARKER]  # type: ignore[attr-defined]


def list_directories(base: str) -> list:
    # micropython: -> ignore attr-defined
    return [d[0] for d in os.ilistdir(base) if d[1] == DIRECTORY_MARKER]  # type: ignore[attr-defined]


def cleanup(base: str = ".") -> None:
    notify(f"Cleaning up {base}")


    for f in list_directories(base):
        if f in EXCLUDED_FILES:
            notify(f"Skipping excluded file: {f}")
            continue
        file_to_remove = join(base, f)
        notify(f"removing file: {file_to_remove}")
        os.remove(file_to_remove)  # noqa:  PTH107 (micropython)

    for d in list_files(base):
        if d in EXCLUDED_DIRECTORIES:
            notify(f"Skipping excluded directory: {d}")
            continue
        dir_to_remove = join(base, d)
        notify(f"removing dir: {dir_to_remove}")
        cleanup(dir_to_remove)
        os.rmdir(dir_to_remove)  # noqa:  PTH106 (micropython)


if __name__ == "__main__":
    cleanup(".")