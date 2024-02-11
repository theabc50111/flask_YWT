from flask import Flask, render_template, request, url_for
from pathlib import Path
import uuid

# practice start
# practice end

app = Flask(__name__)

# practice start
# practice end

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header")

# practice start
# practice end


if __name__ == "__main__":
    app.run(debug=True)



