from flask import Flask

app = Flask(__name__)

#----------practice start------------
@app.route('/')
def index():
    return '<h1>!@#$Bad Request!!!!</h1>', 400, {"key1":100, "key2":200}
#----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)
