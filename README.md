Micropython VS Code devcontainer for ESP32 with Windows 11 support

Important: Before starting this container your USB device must **already be available** to WSL as /dev/ttyUSB0. See the windows_usb_passthrough folder for more details and useful scripts. This is because the container assumes your device is on USB0. 

You need...
1. Docker installed and running, 
2. VS Code plus the Docker Containers extension installed...
 then you can simply fork this repo, bring up the command pallete and start typing "Dev Containers: Clone Repository In Container Volume...". It will automatically be linked to your newly forked git repo.
 3. A device flashed with Micropython

A "project" is simply any folder you create at the default top level of the container volume - eg /workspaces/micropython/Project1.

Why a "devcontainer"?

Dev Containers are useful because they provide a consistent, reproducible, and isolated development environment, ensuring that all developers on a project work with the same dependencies, tools, and configurations. By leveraging containerization (typically using Docker), Dev Containers eliminate "works on my machine" issues, as the development environment is portable and independent of the host operating system. This is particularly valuable for onboarding new team members quickly or working across different projects with conflicting dependencies. Additionally, they integrate seamlessly with editors like Visual Studio Code, enabling developers to work inside the container with access to the same IDE features, extensions, and debugging tools as on the host. Dev Containers also support CI/CD pipelines by allowing developers to align their local environment with the build and test environments, further improving workflow consistency and reliability.

There are plenty of resources explaining how to set up Docker to run a devcontainer so this isn't covered here.
