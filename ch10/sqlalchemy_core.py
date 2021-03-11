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
con = engine.connect()

# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
metadata = db.MetaData()
# 取得 test 資料表的 Python 對應操作物件
table_office = db.Table(table, metadata, autoload=True, autoload_with=engine)

# INSERT
query = db.insert(table_office, ['https://www.google.com/'])
proxy = connection.execute(query)

# UPDATE
query = db.update(tableBeauty).where(tableBeauty.c.url == 'https://www.google.com/').values(url='https://www.facebook.com/')
proxy = connection.execute(query)

# DELETE
query = db.delete(tableBeauty).where(tableBeauty.c.url == 'https://www.facebook.com/')
proxy = connection.execute(query)

# SELECT
query = db.select(table_office)
proxy = connection.execute(query)
results = proxy.fetchall()
print(results)