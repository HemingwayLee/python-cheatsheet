# How
* set it up
```
pip3.7 install py2app
py2applet --make-setup hello.py 
cat setup.py 
python3.7 setup.py py2app
```

* `python3 setup.py py2app` does not work
  * The version of python, the version of each package does make differences

* run it
```
./dist/hello.app/Contents/MacOS/hello
```

# Note
* it works for Mac only
* take care of the filename, it might be conflict with other file within the dependencies

