commands = {
    "bl": "bootloader",
    "xrun script='main.py'": {
        "command": ["exec", "exec( open(script).read() , globals() )"],
        "help": "Run a script on the remote device",
    },
    "littlefs_esp": [
        "exec",
        "--no-follow",
        "import os; os.umount('/'); os.VfsLfs2.mkfs(bdev); os.mount(bdev, '/'); machine.reset()",
    ],
    "ifconfig": [
        "exec",
        "import network; sta_if = network.WLAN(network.STA_IF); print(sta_if.ifconfig())",
    ],
    "hot": [
        "exec",
        "import esp32; raw_temp = esp32.raw_temperature(); print('Degs :', int((raw_temp - 32) / 1.8))",
    ],
}
