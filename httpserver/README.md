# How to run
## http server
```
python3 -m http.server 8888
```

## run cgi
* `hello.py` must be executable, use `chmod`
```
python3 -m http.server --bind localhost --cgi 8000
```

* Access `http://localhost:8000/cgi-bin/hello.py`


