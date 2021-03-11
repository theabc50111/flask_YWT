#----------practice start------------
from flask import Flask, abort
#----------practice end--------------

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hi</h1>"

# ----------practice start------------
@app.route('/user/<int:id_>')
def get_user(id_):
    if id_ > 100:
        abort(404)
    return f'<h1>Hello, No.{id_} user</h1>'
# ----------practice end--------------


if __name__ == '__main__':
    app.run(debug=True)
