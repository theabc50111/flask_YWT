# pracitce start
from flask import Flask, render_template, request, redirect, url_for
# practice end

from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())

@app.route('/prg', methods=['GET','POST'])
def post_redirect_get():
    if request.method=="POST":
        return redirect(url_for("post_redirect_get"))
    data = [["method:", request.method],
            ["base_url:", request.base_url],
            ["form data:", request.form]]
    return render_template('session.html', page_header="Form", data=data)
        

if __name__ == "__main__":
    app.run(debug=True)
