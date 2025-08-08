#!/bin/bash

rm -f __init__.py
pyinstaller main.py --noconsole --onefile --add-binary="/usr/bin/ffmpeg:." --name nameless_convertor
touch __init__.py
