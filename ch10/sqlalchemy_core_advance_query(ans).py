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
# and/or
query = db.select(table_invoices.c.InvoiceId, table_invoices.c.BillingCountry, table_invoices.c.Total).select_from(table_invoices).where(db.and_(table_invoices.c.BillingCountry=="Argentina", table_invoices.c.Total>=2))
proxy = connection.execute(query)
results = proxy.fetchall()
print(f"The cost over 2 dollars in Argentina: {results}",end="\n"+("-"*80)+"\n")
query = db.select(table_invoices.c.InvoiceId, table_invoices.c.BillingCountry, table_invoices.c.Total).select_from(table_invoices).where(db.and_(db.or_(table_invoices.c.BillingCountry=="Argentina", table_invoices.c.BillingCountry=="Poland"), table_invoices.c.Total>=2))
proxy = connection.execute(query)
results = proxy.fetchall()
print(f"The cost over 2 dollars in Argentina or Poland: {results}",end="\n"+("-"*80)+"\n")

# SQL function
query = db.select(func.count()).select_from(table_invoices)
proxy = connection.execute(query)
results = proxy.fetchall()
print(f"Number of invoices: {results}",end="\n"+("-"*80)+"\n")
query = db.select(func.max(table_invoices.c.Total)).select_from(table_invoices)
proxy = connection.execute(query)
results = proxy.fetchall()
print(f"The most expensive invoices: {results}",end="\n"+("-"*80)+"\n")
query = db.select(func.avg(table_invoices.c.Total)).select_from(table_invoices)
proxy = connection.execute(query)
results = proxy.fetchall()
print(f"The average cost of invoices: {results}",end="\n"+("-"*80)+"\n")

# group by
query = db.select(table_invoices.c.BillingCountry, func.sum(table_invoices.c.Total)).select_from(table_invoices).group_by(table_invoices.c.BillingCountry)
proxy = connection.execute(query)
results = proxy.fetchall()
print(f"The sum cost of each country: {results}",end="\n"+("-"*80)+"\n")
query = db.select(table_invoices.c.BillingCountry, func.sum(table_invoices.c.Total)).select_from(table_invoices).where(table_invoices.c.Total > 3).group_by(table_invoices.c.BillingCountry)
proxy = connection.execute(query)
results = proxy.fetchall()
print(f"The sum cost where the cost is larger than 3 dollars of each country: {results}",end="\n"+("-"*80)+"\n")
query = db.select(table_invoices.c.BillingCountry, func.sum(table_invoices.c.Total)).select_from(table_invoices).group_by(table_invoices.c.BillingCountry).having(func.sum(table_invoices.c.Total)>100)
proxy = connection.execute(query)
results = proxy.fetchall()
print(f"The sum cost where the cost is larger than 3 dollars, and sum cost larger than 100 dollars: {results}",end="\n"+("-"*80)+"\n")

# join
j_invoice_customer = table_invoices.join(table_customers, table_invoices.c.CustomerId==table_customers.c.CustomerId)
query = db.select(table_invoices.c.InvoiceDate, table_customers.c.FirstName).select_from(j_invoice_customer).where(table_customers.c.CustomerId==2)
proxy = connection.execute(query)
results = proxy.fetchall()
print(f"Check the customer name and consume date of No.2 customer: {results}",end="\n"+("-"*80)+"\n")

# distinct
query = db.select(table_invoices.c.BillingCountry).distinct().select_from(table_invoices)
proxy = connection.execute(query)
results = proxy.fetchall()
print(f"The recorded countries of invoices: {results}",end="\n"+("-"*80)+"\n")

# raw sql select
raw_query = text("SELECT InvoiceId, Total FROM invoices WHERE Total > 10*(SELECT MIN(Total) FROM invoices)")
proxy = connection.execute(raw_query)
results = proxy.fetchall()
print(f"The cost larger than 10 times of cheapest cost {results}",end="\n"+("-"*80)+"\n")
# raw sql insert
raw_query = text("INSERT INTO genres(GenreId, Name) VALUES(:GenreId, :Name)")  # avoid sql injection 
connection.execute(raw_query, {"GenreId": 30, "Name": "New type music"})
connection.commit()
#----------practice end------------

# Close connection & engine
connection.close()
engine.dispose()