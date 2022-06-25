#----------practice start------------
from flask import Flask, redirect
#----------practice end--------------

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>try change url to /redirect</h1>"

#----------practice start------------
@app.route('/redirect')
def red():
    return redirect('http://www.example.com')
#----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)
