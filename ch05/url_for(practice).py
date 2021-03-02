from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

@app.route('/user/<name>')
def user(name):
    return render_template('delimiters.html')

#----------practice start------------

#----------practice end-------------- 


if __name__=="__main__":
    app.run(debug=True)
