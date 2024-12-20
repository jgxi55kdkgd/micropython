#!/bin/bash

# Function to validate the directory name
is_valid_directory() {
  echo $1
  local dir_name=$1
  # Check if it's not empty, not ".", not "..", and exists under $WSHOME
  [[ -n "$dir_name" && "$dir_name" != "." && "$dir_name" != ".." && -d "$dir_name" ]]
}

# Prompt the user for the directory name if no argument is provided
if [ -z "$1" ]; then
  while true; do
    read -p "Please enter the directory name of the project in ${WSHOME}/: " project_dir
    if is_valid_directory "${WSHOME}/$project_dir"; then
      push="${WSHOME}/${project_dir}"
      break
    else
      echo "Invalid directory: ${WSHOME}/${project_dir}"
      echo "Please try again. Ensure it is a valid directory under ${WSHOME}/."
    fi
  done
else
  echo "${WSHOME}/$1"
  if is_valid_directory "${WSHOME}/$1"; then
    push="${WSHOME}/${1}"
  else
    echo "Error: ${WSHOME}/${1} is not a valid project directory."
    exit 1
  fi
fi

# Check for libs.manifest file
LIBS_MANIFEST="$push/libs.manifest"
if [ ! -f "$LIBS_MANIFEST" ] || [ ! -s "$LIBS_MANIFEST" ]; then
  echo "No libs to install."
  exit 0
fi

# Install Wi-Fi password script
${WSHOME}/utils/install_wifi_pw.py

# Start Wi-Fi
mpremote u0 run ${WSHOME}/utils/start_wifi.py

# Iterate over each line in libs.manifest and install libraries
while IFS= read -r lib; do
  if [ -n "$lib" ]; then
    echo "Installing library: $lib"
    mpremote u0 mip install "$lib"
  fi
done < "$LIBS_MANIFEST"

# Stop Wi-Fi
mpremote u0 run ${WSHOME}/utils/stop_wifi.py
