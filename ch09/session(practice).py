# practice start

# practice end

from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)

# practice start

# practice end

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())

# practice start

# practice end
 

if __name__ == "__main__":
    app.run(debug=True)
