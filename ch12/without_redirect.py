from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())

@app.route('/without_redirect', methods=['GET','POST'])
def without_redirect():
    data = [["method:", request.method],
            ["base_url:", request.base_url],
            ["form data:", request.form]]
    return render_template('session.html', page_header="Form", data=data)



if __name__ == "__main__":
    app.run(debug=True)
