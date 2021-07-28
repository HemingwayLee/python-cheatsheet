#!/bin/bash

# codesign -a x86_64 -s "Code Signing Test" $(pwd)
codesign -s "Code Signing Test" $(pwd)

# uppercase matters
# in venv, we need to use python3
python3.7 -m PyInstaller hello.py

