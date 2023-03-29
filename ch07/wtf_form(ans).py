from flask import Flask, render_template, request
from flask_moment import Moment
from datetime import datetime

# practice start
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
# practice end

app = Flask(__name__)
moment = Moment(app)

# practice start
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    password = StringField('password?')
    gender = RadioField('gender?', choices=[1, 2])
    submit = SubmitField('Submit')
# practice end

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())

# practice start
@app.route('/wtf_form', methods=['GET', 'POST'])
def wtf_form():
    form = NameForm()
    if request.method == "GET":
        return render_template('wtf_form.html', page_header="wtFrom", form=form)
    else:
        data = [["method:", request.method],
                ["base_url:", request.base_url],
                ["form data:", request.form]]
        return render_template('form_result.html',
                               page_header="Form data", data=data)
# practice end

if __name__ == "__main__":
    app.run(debug=True)
