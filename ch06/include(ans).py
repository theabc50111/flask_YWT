from flask import Flask, render_template


app = Flask(__name__)



#----------practice start------------
@app.route('/')
def index():
    return render_template("include.html")
#----------practice end-------------- 


if __name__=="__main__":
    app.run(debug=True)
