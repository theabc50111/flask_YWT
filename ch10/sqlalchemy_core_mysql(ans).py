#----------practice start------------
import sqlalchemy as db

#連接資料庫
username = 'root'     # 資料庫帳號
password = ''     # 資料庫密碼
host = 'localhost'    # 資料庫位址
port = '3306'         # 資料庫埠號
database = 'classicmodels'   # 資料庫名稱
table = 'offices'   # 表格名稱
# 建立資料庫引擎
engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
# 建立資料庫連線
# con = engine.raw_connection()
connection  = engine.connect()

# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
metadata = db.MetaData()

# 取得 office 資料表的 Python 對應操作物件
table_office = db.Table(table, metadata, autoload=True, autoload_with=engine)
print(f"metadata: \n{metadata.sorted_tables}") 

# SELECT
query = db.select(table_office)
proxy = connection.execute(query)
results = proxy.fetchall()
print(results)

# INSERT
query = db.insert(table_office, ["8", 'Taipei', '+886 02 6631 6666', 'No.390, Sec. 1, Fusing S. Rd., Da’an Dist.', 'Floor #2', None, 'ROC', '106470', 'ROC'])
proxy = connection.execute(query)

# UPDATE
query = db.update(table_office).where(table_office.c.officeCode == '5').values(addressLine2='Floor #6')
proxy = connection.execute(query)

# INSERT
floors = ['Floor #3', 'Floor #4', 'Floor #5', 'Floor #6', 'Floor #7', 'Floor #8', 'Floor #9', 'Floor #10', 'Floor #11', 'Floor #12', 'Floor #13']
for i,floor in enumerate(floors):
    query = db.insert(table_office, [str(i+9), 'Taipei', '+886 02 6631 6666', 'No.390, Sec. 1, Fusing S. Rd., Da’an Dist.', floor, None, 
                                    'ROC', '106470', 'ROC'])
    proxy = connection.execute(query)

# DELETE
from sqlalchemy import Integer
query = db.delete(table_office).where(table_office.c.officeCode.cast(Integer) >15)
proxy = connection.execute(query)
#----------practice end--------------

# -----------UPDATE seq and restore database--------------
# query = db.update(table_office).where(table_office.c.officeCode == "5").values(addressLine2=None)
# proxy = connection.execute(query)
# from sqlalchemy import Integer
# query = db.delete(table_office).where(table_office.c.officeCode.cast(Integer) >7)
# proxy = connection.execute(query)
# -----------UPDATE seq and restore database--------------

