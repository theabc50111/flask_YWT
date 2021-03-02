from flask import Flask, request,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hi"

# ----------practice start------------
@app.route("/req")
def req():
    data = [["args:", request.args],
           ["values:", request.values],
           ["cookies:", request.cookies],
           ["headers:", request.headers],
           ["host:", request.host],
           ["method:", request.method],
           ["path:", request.path],
           ["query_string:", request.query_string],
           ["full_path:", request.full_path],
           ["url:", request.url],
           ["base_url:", request.base_url],
           ["remote_addr:", request.remote_addr]]
    return render_template("req_obj.html",data=data)
# ----------practice end--------------


if __name__ == '__main__':
    app.run(debug=True)
