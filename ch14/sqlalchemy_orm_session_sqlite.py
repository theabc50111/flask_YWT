from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

if __name__ == '__main__':
    engine = create_engine('sqlite://///home/ywt01/Documents/codes/flask_eg_YWT/ch10/db/test.db', echo=True)

    ''' 真正建立表格是使用 Base.metadata.create_all(engine) '''
    Base.metadata.create_all(engine)

    SqlalchemySession = sessionmaker(bind=engine)
    db_session = SqlalchemySession()

    user_a = User('user1', 'username', 'userpassword'.encode('utf-8'))
    db_session.add(user_a)
    db_session.commit()

