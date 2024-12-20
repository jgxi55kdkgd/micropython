#!/bin/bash

# Optional additional configuration script
echo "Setting up mpremote customised commands in home/vscode/.config/mpremote/config.py"
ln -s $(pwd)/utils/.config/mpremote /home/vscode/.config/mpremote
# install stubs so we don't get Pylance errors when importing "machine" etc
ln -s /home/vscode/typings $(pwd)/typings
# Set up our alises
cp .bash_aliases ~/
echo "export WSHOME=$(pwd)" >> ~/.bashrc
. ~/.bashrc

echo "Useful commands...."
cat .bash_aliases

echo "Devices connected:"
mpremote devs

