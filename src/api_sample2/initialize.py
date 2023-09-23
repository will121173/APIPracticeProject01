import sqlite3
from dbutils import *

# データベース sample2.db への接続。存在しない場合は暗黙的に作成します。
con = sqlite3.connect("sample2.db")

# Records作成
# テーブルが存在する場合も強制的にリセットします
# AccountingDateは yyyy-mm-dd形式
cur = con.cursor()
try: cur.execute("DROP TABLE Records;")
except: pass
sql = """
    CREATE TABLE Records (
        Id  INTEGER PRIMARY KEY,
        Price INTEGER,
        ItemName VARCHAR(100),
        AccountingDate VARCHAR(10),
        CreateUserId INTEGER
    );
"""
cur.execute(sql)

# Users作成
# テーブルが存在する場合も強制的にリセットします
try: cur.execute("DROP TABLE Users;")
except: pass
sql = """
    CREATE TABLE Users (
        Id  INTEGER PRIMARY KEY,
        UserName VARCHAR(100)
    );
"""
cur.execute(sql)

# サンプルデータ作成
InsertUser(con,('sample user',))
InsertRecord(con,(100,"sample1","2000-01-01",1))
InsertRecord(con,(200,"sample2","2000-01-02",1))
InsertUser(con,('サンプルユーザー２',))
InsertRecord(con,(10000,"sample3","2000-01-03",2))
InsertRecord(con,(20000,"sample4","2000-01-04",2))

# サンプルデータ表示
print(cur.execute("select * from Records;").fetchall())
print(cur.execute("select * from Users;").fetchall())
con.close()
