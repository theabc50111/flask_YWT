from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

#----------practice start------------
@app.route('/test_static')
def test_static():
    print(app.url_map)
    return render_template('static.html')
#----------practice end-------------- 


if __name__=="__main__":
    app.run(debug=True)
