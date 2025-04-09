from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import sqlalchemy as db
from sqlalchemy import func
import math


app = Flask(__name__)

# sql setting
path_to_db = "./db/chinook.db"
table = 'customers'
engine = db.create_engine(f'sqlite:///{path_to_db}')
metadata = db.MetaData()
table_customers = db.Table(table, metadata, autoload=True, autoload_with=engine)

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())


#----------practice start------------

#----------practice end--------------

if __name__ == "__main__":
    app.run(debug=True)