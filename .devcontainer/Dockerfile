ARG VARIANT=bookworm
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get -y install --no-install-recommends \
        udev \
        # uncomment lines below if you want to use Pymakr and install the extension
        #nodejs \
        #npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# we need these useful tools
RUN pip install esptool mpremote black --no-user
# give permission to vscode to use the USB device
RUN usermod -aG plugdev,dialout vscode

# install local python stubs to avoid some Pylance error messages and set up autocomplete
USER vscode
RUN pip install micropython-esp32-stubs --no-user --target /home/vscode/typings


