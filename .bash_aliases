alias ll='ls -l'
alias mp='mpremote'
alias esp="esptool.py -p /dev/ttyUSB0 chip_id" 
    # query your esp32 processor details
mpx() {
    local folder=${1:-.}  # Use the argument passed to the function, default to "."
    mpremote mount "$folder" exec "import main"
}
    # mount a folder of my choice onto the device and run main.py in that folder
    # note that the folder gets mounted as /remote but the lib path will still use /lib
alias mpformat='mpremote xrun'
    # executes main.py on the ESP32. Unlike mpremote run it doesn't copy the file over
alias mpformat='mpremote littlefs_esp' 
    # reformat the filesystem and start again (quick way of rm -r)
alias mpip='mpremote ifconfig' 
    # find out your wifi IP address, router and mask
alias mpls='mpremote ls' 
    # list the files on your esp32
alias mprepl='mpremote repl' 
    # enter REPL mode on your ESP32
alias mptidy='mpremote run ${WSHOME}/utils/clean_mc_fs.py' 
    # Remove all files on your ESP32 except "lib" and secrets.py (configurable)
alias mpgetlib='${WSHOME}/utils/download_libs.sh' 
    # pull the lib folder from your device down into local project folder
alias mppush='${WSHOME}/utils/install_code.sh' 
    # push code from your project folder to ESP32 except files/dirs listed in .mpignore
alias mpputlib='${WSHOME}/utils/install_libs.sh' 
    # installs libs listed in your libs.manifest file directly onto ESP32
alias mpwifipw='${WSHOME}/utils/install_wifi_pw.py' 
    # installs your WiFi SSID and Password onto ESP32 as /secrets.py
alias mpwifigo='mpremote u0 run ${WSHOME}/utils/start_wifi.py' 
    # starts WiFi on your ESP32 (needs secrets.py)
alias mpwifistop='mpremote u0 run ${WSHOME}/utils/stop_wifi.py' 
    # stops WiFI on your ESP32
alias mpreset='mpremote reset' 
    # reset ESP32

