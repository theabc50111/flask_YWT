from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

#----------practice start------------
@app.route('/import')
def import_page():
    data = [["title1","item1"],["title2","item2"],["title3","item3"]]
    return render_template("import.html",data_jinja=data)
#----------practice end--------------

if __name__=="__main__":
    app.run(debug=True)