from runner import foo 
import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World 2'

@app.route('/ai')
def run_ai():
    return foo()

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)





