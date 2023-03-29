from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = hashlib.sha1(password).hexdigest()

    def __repr__(self):
        return "User('{}','{}', '{}')".format(
            self.name,
            self.username,
            self.password
        )


if __name__ == '__main__':
    ''' 此時只有建立 SQLAlchemy Engine 實例，還沒在記憶體內建立資料，
        只有第一個 SQL 指令被下達時，才會真正連接到資料庫內執行 '''
    engine = create_engine('sqlite://///home/ywt01/Documents/codes/flask_eg_YWT/ch10/db/test.db', echo=True)

    ''' 真正建立表格是使用 Base.metadata.create_all(engine) '''
    Base.metadata.create_all(engine)

    auser = User('user1', 'username', 'userpassword'.encode('utf-8'))
    print('Mapper:', auser.__mapper__)
    print('Mapper:', auser.__table__)