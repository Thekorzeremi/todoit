#!/bin/bash
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found, please install it."
    exit
fi
if ! command -v pip3 &> /dev/null
then
    echo "pip3 could not be found, please install it."
    exit
fi
pip3 install pystray pillow
echo "Installation complete. You can now run the application using start.sh."
echo "To uninstall, simply delete the application folder."