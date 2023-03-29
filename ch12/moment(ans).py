# practice start
from flask import Flask, render_template, Markup # Markup() would trust the string that pass to it without escaping.
from datetime import datetime
# practice end

app = Flask(__name__)

# practice start
start_time = datetime(2021, 1, 1, 12, 0, 0)

class MomentJSFlask():
    def __init__(self, timestamp, element_id):
        self.timestamp = timestamp
        self.element_id = element_id
    # Wrapper to call moment.js method
    
    def render(self, func_str):
        return Markup(
            f"""
                document.querySelector('#{self.element_id}').innerText = moment('{self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}').{func_str};
            """
        )
    # Format time
    def format(self, fmt):
        return self.render(f'format("{fmt}")')

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")

app.jinja_env.globals['momentjs_flask'] =  MomentJSFlask


@app.route('/')
def index():
    return render_template('moment.html',
                           page_header="page_header",
                           start_time=start_time)
# practice end

if __name__=="__main__":
    app.run(debug=True)
