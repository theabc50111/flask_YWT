import sqlalchemy as db

# 建立資料庫引擎
engine = db.create_engine('mysql+mysqlconnector://root:root@localhost:3306/crawler')
# 建立資料庫連線
connection = engine.connect()
# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
metadata = db.MetaData()
# 取得 test 資料表的 Python 對應操作物件
tableBeauty = db.Table('beauties', metadata, autoload=True, autoload_with=engine)

# INSERT
query = db.insert(tableBeauty, ['https://www.google.com/'])
proxy = connection.execute(query)

# UPDATE
query = db.update(tableBeauty).where(tableBeauty.c.url == 'https://www.google.com/').values(url='https://www.facebook.com/')
proxy = connection.execute(query)

# DELETE
query = db.delete(tableBeauty).where(tableBeauty.c.url == 'https://www.facebook.com/')
proxy = connection.execute(query)

# SELECT
query = db.select([tableBeauty])
proxy = connection.execute(query)
results = proxy.fetchall()
print(results)