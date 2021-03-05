# ----------practice start------------
from flask import Flask, escape
# ----------practice end--------------

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# ----------practice start------------
@app.route('/escape')
def with_escape():
    return escape("<h1>With escape()</h1>")
            

@app.route('/not_escape')
def not_with_escape():
    return "&lt;h1&gt;Not with escape()&lt;/h1&gt;"
# ----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)