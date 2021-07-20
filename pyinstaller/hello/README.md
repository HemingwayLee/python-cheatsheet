# On mac, we have code sign issue
* follow [readme](https://github.com/pyinstaller/pyinstaller/wiki/Recipe-OSX-Code-Signing) to make a self-signed certificate

```
codesign -s "Code Signing Test" /Users/Rosemary/Desktop/code/projects/python-cheatsheet/pyinstaller/hello
touch Info.plist 
pyinstaller hello.py
```

* The content of `Info.plist`
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


# with docker (on linux)
```
docker build -t mypyinstaller .
docker run -it --rm mypyinstaller
```

