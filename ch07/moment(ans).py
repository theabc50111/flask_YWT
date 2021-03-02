# practice start
from flask import Flask, render_template, Markup
from datetime import datetime
# practice end

app = Flask(__name__)

# practice start
start_time = datetime(2021, 1, 1, 12, 0, 0)

class momentjs():
    def __init__(self, timestamp):
        self.timestamp = timestamp
    # Wrapper to call moment.js method
    
    def render(self, func_str):
        return Markup(
            f"""
            <script>
                document.write(moment('{self.timestamp.strftime("%Y-%m-%dT%H:%M:%S")}').{func_str}) ;
            </script>
            """
        )
    # Format time
    def format(self, fmt):
        return self.render(f'format("{fmt}")')

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")

app.jinja_env.globals['momentjs'] = momentjs


@app.route('/')
def index():
    return render_template('moment.html',
                           page_header="page_header",
                           start_time=start_time)
# practice end

if __name__=="__main__":
    app.run(debug=True)
