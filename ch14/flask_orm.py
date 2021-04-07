from flask import Flask, render_template, request
from flask_moment import Moment
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'sqlite://///home/ywt01/Documents/codes/flask_eg_YWT/ch10/db/test.db', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "User('{}','{}', '{}')".format(
            self.name,
            self.email,
            self.password
        )


app = Flask(__name__)
moment = Moment(app)
Base.metadata.create_all(engine)

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())

# practice start
@app.route('/form', methods=['POST', "GET"])
def get_form():
    
    return render_template('form.html', page_header="Form")
    
        

@app.route('/form_result', methods=['POST']) # default methods is "GET"
def form_result():
    SqlalchemySession = sessionmaker(bind=engine)
    db_session = SqlalchemySession()
    user = User(request.form.get("name"), request.form.get("email"), request.form.get("password"))
    # db_session.add(user)
    db_session.commit()
    if db_session.query(User).filter_by(name=request.form.get("name")).first():
        insert_sucess=True
    else:
        insert_sucess=False
    data = [["method:", request.method],
            ["base_url:", request.base_url],
            ["form data:", request.form]]
    return render_template('form_result.html', page_header="Form data", data=data, insert_sucess=insert_sucess)

if __name__ == '__main__':
    app.run(debug=True)
