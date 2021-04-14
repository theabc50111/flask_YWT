#----------practice start------------
from flask import Flask, make_response
#----------practice end--------------
import os

app = Flask(__name__)

#----------practice start------------
@app.route('/')
def index():
    response = make_response('<h1>Check the status code</h1>')
    response.status_code = 200
    print(response.conten_length, len("<h1>Check the status code</h1>"))
    return response
#----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)