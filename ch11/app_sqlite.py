from flask import Flask, render_template, request, redirect, url_for, session
from flask_moment import Moment
from datetime import datetime
import sqlalchemy as db
from sqlalchemy import func
import math


app = Flask(__name__)
moment = Moment(app)

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


@app.route('/data-list')
def data_list():

    # query string
    page = int(request.args.get('page') if request.args.get('page') else 1)
    each_page = 5

    # set total pages
    connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
    query = db.select(func.count()).select_from(table_customers)
    proxy = connection.execute(query)
    total_pages = math.ceil(proxy.fetchall()[0][0]/each_page) # [0][0] => inorder to get the value

    # fetch data & decided by page
    query = db.select(table_customers).limit(each_page).offset((page-1)*each_page)
    proxy = connection.execute(query)
    results = proxy.fetchall()
    print(results[1].keys())

    # Close connection
    connection.close()
    
    return render_template('data_list.html',
                           page_header="list all data",
                           total_pages=total_pages,
                           outputs=results,
                           page=page)

@app.route('/data-edit', methods=["GET", "POST"])
def data_edit():
    if request.method=="POST":
        try:
            connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
            query = db.select(table_customers.c.CustomerId).order_by(table_customers.c.CustomerId)
            proxy = connection.execute(query)
            id_list = [idx[0] for idx in proxy.fetchall()]
            if request.form['FirstName']: # 希望至少要填寫名子
                query = db.update(table_customers).where(table_customers.c.CustomerId == request.form['CustomerId']).values(**{k:request.form[k] for k in request.form.keys()})
                proxy = connection.execute(query)
            else:
                raise Exception
        except:
            return render_template('data_edit.html',
                                    page_header="edit data",id_list=id_list,status="Failed")
        else:
            return render_template('data_edit.html',
                                    page_header="edit data",id_list=id_list,status="Success")
        finally:
            # Close connection
            connection.close()
           
    if request.method=="GET":
        connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
        query = db.select(table_customers.c.CustomerId).order_by(table_customers.c.CustomerId)
        proxy = connection.execute(query)
        id_list = [idx[0] for idx in proxy.fetchall()]
        connection.close()
        return render_template('data_edit.html',
                                page_header="edit data",id_list=id_list)

if __name__ == "__main__":
    app.run(debug=True)