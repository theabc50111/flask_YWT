#----------practice start------------
import sqlalchemy as db

#連接資料庫
path_to_db = "./db/chinook.db"
table = 'genres'   # 表格名稱
# 建立資料庫引擎
engine = db.create_engine(f'sqlite:///{path_to_db}')
# 建立資料庫連線
connection  = engine.connect()

# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
metadata = db.MetaData()

# 取得 genres 資料表的 Python 對應操作物件
table_genres = db.Table(table, metadata, autoload=True, autoload_with=engine)
print(f"metadata: \n{metadata.sorted_tables}") 

# SELECT
query = db.select(table_genres)
proxy = connection.execute(query)
results_all = proxy.fetchall()
print(results_all)

# INSERT
query = db.insert(table_genres).values(Name='Funk')
proxy = connection.execute(query)

# UPDATE
query = db.update(table_genres).where(table_genres.c.GenreId == 9).values(Name='K-pop')
proxy = connection.execute(query)

# INSERT
for value in ['Funk2','Funk3','Funk4','Funk5','Funk6']:
    query = db.insert(table_genres).values(Name=value)
    proxy = connection.execute(query)


# DELETE
query = db.delete(table_genres).where(table_genres.c.GenreId > 28)
proxy = connection.execute(query)
#----------practice end--------------


# -----------UPDATE seq and restore database--------------
# query = db.update(table_genres).where(table_genres.c.GenreId == 9).values(Name='Pop')
# proxy = connection.execute(query)
# query = db.delete(table_genres).where(table_genres.c.GenreId > 25)
# proxy = connection.execute(query)
# table_seq = db.Table("sqlite_sequence", metadata, autoload=True, autoload_with=engine)
# query = db.update(table_seq).where(table_seq.c.name == "genres").values(seq=25)
# proxy = connection.execute(query)
# -----------UPDATE seq and restore database--------------


