from flask import Flask, escape


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# ----------practice start------------
@app.route('/user/<name>/<path:id_>')
def user_check_type(name, id_):
    return (f'<h1>id: {escape(id_)}!</h1>'
            f'<h1>name: {escape(type(name))}!</h1>')
# ----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)