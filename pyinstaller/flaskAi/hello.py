from runner import foo 
import os
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(['Hello', 'World', '2'])

@app.route('/ai')
def run_ai():
    return jsonify(foo())

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)





