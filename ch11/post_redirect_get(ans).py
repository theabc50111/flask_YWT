# practice start
from flask import Flask, render_template, request, redirect, url_for
# practice end

from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())

# practice start
@app.route('/prg', methods=['GET','POST'])
def post_redirect_get():
    if request.method=="POST":
        app.logger.info(f'{request.form}') # in order to check if request.form has data
        return redirect(url_for("post_redirect_get"))
    data = [["method:", request.method],
            ["base_url:", request.base_url],
            ["form data:", request.form]]
    return render_template('session.html', page_header="Form", data=data)
# practice 


if __name__ == "__main__":
    app.run(debug=True)
