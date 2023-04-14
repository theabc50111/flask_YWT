from flask import Flask, render_template, request
from datetime import datetime

# practice start
# practice end

app = Flask(__name__)

# practice start
# practice end

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header")


# practice start
# practice end


if __name__ == "__main__":
    app.run(debug=True)
