from flask import Flask, escape


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# ----------practice start------------
# ----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)