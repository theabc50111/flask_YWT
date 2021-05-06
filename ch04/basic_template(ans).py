#----------practice start------------
from flask import Flask, render_template
#----------practice end--------------

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

#----------practice start------------
@app.route('/user/<name>')
def user(name):
    return render_template('delimiters.html',name_jinja=name)

@app.route("/filter/<var>")
def test_filter(var):
    safe_var = "<h3>456</h3>"
    return render_template("filter.html", var_jinja=var, safe_var_jinja=safe_var)


@app.route('/if/<name>')
def user_if(name):
    if name=="YWT":
        user=name
    else:
        user=None
    return render_template('if.html', user_jinja=user)

@app.route('/for')
def user_for():
    lines = ["line1","line2","line3"]
    return render_template('for.html', Lines=lines)
#----------practice end-------------- 


if __name__=="__main__":
    app.run(debug=True)
