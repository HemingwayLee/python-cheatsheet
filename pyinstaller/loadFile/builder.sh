#!/bin/bash

# codesign -a x86_64 -s "Code Signing Test" $(pwd)
codesign -s "Code Signing Test" $(pwd)

# uppercase matters
python3.7 -m PyInstaller hello.py

