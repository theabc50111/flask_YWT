#----------practice start------------
from flask import Flask, render_template, url_for
#----------practice end--------------

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

@app.route('/user/<name>')
def user(name):
    return render_template('delimiters.html')

#----------practice start------------
@app.route('/url_for')
def test_urlfor():
    print(app.url_map)
    return render_template('url_for.html')
#----------practice end-------------- 


if __name__=="__main__":
    app.run(debug=True)
