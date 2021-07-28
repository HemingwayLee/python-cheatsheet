# On mac, we have code sign issue
```
pyinstaller hello.py
```

* Not working now...

## Note
* `tensorflow_core` only exists in 1.15, 2.0 and 2.1
* `tensorflow.contrib` only exists in 1.15

# with docker (on linux)
```
docker build -t mypyinstaller .
docker run -it --rm mypyinstaller
```

