from flask import Flask, request

app = Flask(__name__)


#----------practice start------------
@app.route('/')
def index():
    url = request.url
    return f'<p>link is {url}</p>'
#----------practice end--------------

if __name__ == '__main__':
    app.run(debug=True)


