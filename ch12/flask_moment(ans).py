from flask import Flask, render_template
# practice start
from flask_moment import Moment
from datetime import datetime
# practice end

app = Flask(__name__)

# practice start
moment = Moment(app)
start_time = datetime(2018, 1, 31, 0, 0, 0)

@app.route('/')
def index():
    return render_template('flask_moment.html',
                           page_header="page_header",
                           current_time=datetime.utcnow(),
                           start_time=start_time)
# practice end

if __name__=="__main__":
    app.run(debug=True)
