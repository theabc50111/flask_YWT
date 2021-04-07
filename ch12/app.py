from flask import Flask, render_template, request, url_for
from flask_moment import Moment
from datetime import datetime
import os
import uuid

# practice start
import recognition.load_model as model
# practice end

app = Flask(__name__)
moment = Moment(app)

# practice start
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))+'/static/img/uploaded'
# practice end

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())

# practice start
@app.route('/rec', methods=['GET', 'POST'])
def get_file():
    if request.method == "GET":
        return render_template('file.html', page_header="upload hand write picture")
    elif request.method == "POST":
        file = request.files['file']
        if file:
            filename = str(uuid.uuid5(uuid.NAMESPACE_OID, file.filename))+"_"+file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            predict = model.recog_digit(filename)
        return render_template('recog_result.html', page_header="hand writing digit recognition", predict = predict, src = url_for('static', filename=f'img/uploaded/{filename}'))
# practice end


if __name__ == "__main__":
    app.run(debug=True)
