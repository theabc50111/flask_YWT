from flask import Flask, render_template
# practice start
from flask_moment import Moment
from datetime import datetime
# practice end

app = Flask(__name__)

# practice start
moment = Moment(app)

@app.route('/')
def index():
    return render_template('moment.html',
                           current_time=datetime.utcnow())
# practice end

if __name__=="__main__":
    app.run(debug=True)