#----------practice start------------
from flask import Flask
#----------practice end--------------

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hi</h1>"

# ----------practice start------------
# ----------practice end--------------


if __name__ == '__main__':
    app.run(debug=True)
