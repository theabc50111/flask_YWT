import sqlalchemy as db
from sqlalchemy import func
from sqlalchemy.sql import text

#連接資料庫
path_to_db = "./db/chinook.db"
# 建立資料庫引擎
engine = db.create_engine(f'sqlite:///{path_to_db}')
# 建立資料庫連線
connection  = engine.connect()

# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
metadata = db.MetaData()
# 取得 genres 資料表的 Python 對應操作物件
table_customers = db.Table('customers', metadata, autoload_with=engine)
table_invoices = db.Table('invoices', metadata, autoload_with=engine)


#----------practice start------------
#----------practice end------------

# Close connection & engine
connection.close()
engine.dispose()