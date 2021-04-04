# pracitce start
from flask import Flask, render_template, request, redirect, url_for
# practice end

from flask_moment import Moment
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())