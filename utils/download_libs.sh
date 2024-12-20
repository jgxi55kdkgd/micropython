#!/bin/bash
# Download the lib folder on the microcontroller to our project dir
# Takes an argument of a valid project folder (not . or .. etc)

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

# Perform the desired command
mpremote cp -r :lib $push
