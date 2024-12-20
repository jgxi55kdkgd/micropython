import re
import subprocess
import sys
import time

CONNECTED_REGEX = re.compile(
    r'^(?P<busid>\S+)\s+'
    r'(?P<vidpid>\S+)\s+'
    r'(?P<device>.*?)\s{2,}'
    r'(?P<state>Not shared|Shared|Attached)\s*$'
)

MCU_SUBSTRINGS = ("Silicon Labs CP210x", "USB-SERIAL CH340", "Arduino", "ESP32")

def run_usbipd_command(command_args, admin=False):
    if admin:
        ps_args = [
            "powershell",
            "-Command",
            "Start-Process",
            "powershell",
            "-Verb",
            "RunAs",
            "-ArgumentList",
            f"'usbipd {' '.join(command_args)}'"
        ]
        subprocess.run(ps_args, shell=True)
    else:
        full_cmd = ["usbipd"] + command_args
        subprocess.run(full_cmd, shell=True)

def main():
    try:
        output = subprocess.check_output(["usbipd", "list"], text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print("Failed to retrieve 'usbipd list' output.")
        print(e.output)
        sys.exit(1)

    lines = output.splitlines()
    connected_section = False
    found = None

    for line in lines:
        if line.strip().startswith("Connected:"):
            connected_section = True
            continue
        if line.strip().startswith("Persisted:"):
            break

        if connected_section:
            match = CONNECTED_REGEX.match(line)
            if match:
                device_field = match.group('device')
                if any(sub in device_field for sub in MCU_SUBSTRINGS):
                    found = match
                    break

    if not found:
        print("No matching microcontroller board detected in the Connected section.")
        return

    hardware_id = found.group('vidpid')
    device_name = found.group('device')
    device_state = found.group('state')

    print(f"Detected board: {device_name}")
    print(f"Hardware ID: {hardware_id}")
    print(f"Current state: {device_state}")
    print("[B] Bind & Attach  [D] Detach Only  [U] Detach & Unbind  [Q] Quit")
    choice = input("Enter B, D, U, or Q: ").strip().upper()

    if choice == 'B':
        if device_state == 'Attached':
            print("Board is already attached. No action needed.")
        elif device_state == 'Shared':
            print("Board is already bound. Attaching...")
            run_usbipd_command(["attach", "--wsl", "--hardware-id", hardware_id], admin=False)
        else:
            print("Binding (admin required)...")
            run_usbipd_command(["bind", "--hardware-id", hardware_id], admin=True)

            time.sleep(2)

            print("Attaching (non-admin)...")
            run_usbipd_command(["attach", "--wsl", "--hardware-id", hardware_id], admin=False)

    elif choice == 'D':
        # Detach only, leaving the board in the "Shared" state if it was attached.
        # If it's not currently attached, do nothing.
        if device_state == 'Attached':
            print("Detaching (non-admin), board remains bound (Shared).")
            run_usbipd_command(["detach", "--hardware-id", hardware_id], admin=False)
        else:
            print("Board is not attached. No detach action needed.")

    elif choice == 'U':
        # Detach & Unbind
        if device_state == 'Attached':
            print("Detaching (non-admin)...")
            run_usbipd_command(["detach", "--hardware-id", hardware_id], admin=False)

            print("Unbinding (admin required)...")
            run_usbipd_command(["unbind", "--hardware-id", hardware_id], admin=True)
        elif device_state == 'Shared':
            print("Board is shared but not attached. Unbinding (admin required)...")
            run_usbipd_command(["unbind", "--hardware-id", hardware_id], admin=True)
        else:
            print("Board is not shared. No action needed.")

    else:
        print("No action taken.")

if __name__ == "__main__":
    main()
