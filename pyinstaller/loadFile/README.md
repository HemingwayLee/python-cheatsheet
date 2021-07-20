# On mac, we have code sign issue
* follow [readme](https://github.com/pyinstaller/pyinstaller/wiki/Recipe-OSX-Code-Signing) to make a self-signed certificate

* can not use `.`, we need to use full path
```
codesign -s "Code Signing Test" $(pwd)
touch Info.plist 
pyinstaller hello.py
```

## The content of `Info.plist`
```xml
<plist version="1.0">
<dict>
    <key>CFBundleIdentifier</key>
    <string>com.mycompany.department.appname</string>
    <key>CFBundleName</key>
    <string>CodeSignTest</string>
</dict>
</plist>
```

## Problem
* It is not working for Mac currently
* it is not stable, does not work for some version of 3rd party library

# with docker (on linux)
```
docker build -t mypyinstaller .
docker run -it --rm mypyinstaller
```

