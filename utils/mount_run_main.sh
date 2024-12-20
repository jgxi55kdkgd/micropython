#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Error: No directory name provided."
  exit 1
fi

mpremote mount ../${1} exec "import main"