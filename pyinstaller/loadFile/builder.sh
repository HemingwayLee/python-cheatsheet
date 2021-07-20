
codesign -a x86_64 -s "Code Signing Test" $(pwd)

pyinstaller hello.py

