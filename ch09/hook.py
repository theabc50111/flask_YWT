from flask import Flask, render_template, request, redirect, url_for, session
from flask_moment import Moment
from datetime import datetime, timedelta

app = Flask(__name__)
moment = Moment(app)


app.config['SECRET_KEY'] = 'hard to guess string'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

# practice start
@app.after_request
def clear_session(response):
    if request.form.get("session") and request.form["session"]=="True":
        session.clear()
    return response
# practice end


@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())

@app.route('/session', methods=['GET','POST'])
def get_session():
    if request.method=="POST":
        session["form_data"]=request.form
        return redirect(url_for("get_session"))
    if not session.get("li1"):
        session["li1"]=[1,2,3]
    else:
        session["li1"].append(4)
        session.modified = True
    data = [["method:", request.method],
            ["base_url:", request.base_url],
            ["form data:", request.form],
            ["session:",session],
            ["session['form_data']:",session.get("form_data")]]
    return render_template('hook.html', page_header="Form", data=data)
        

if __name__ == "__main__":
    app.run(debug=True)
