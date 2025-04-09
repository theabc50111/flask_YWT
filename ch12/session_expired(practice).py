from flask import Flask, render_template, request, redirect, url_for, session
# practice start

# practice end



app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

# practice start

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
    data = [["method:", request.method],
            ["base_url:", request.base_url],
            ["form data:", request.form],
            ["session:",session],
            ["session['form_data']:",session.get("form_data")]]
    return render_template('session.html', page_header="Form", data=data)
        

if __name__ == "__main__":
    app.run(debug=True)
