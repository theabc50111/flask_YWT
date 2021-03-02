#----------practice start------------
from flask import Flask, request, make_response
#----------practice end--------------

app = Flask(__name__)

#----------practice start------------
@app.route('/')
def index():
    response = make_response('<h1>Check the status code</h1>')
    response.status_code = 200
    return response
#----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)
