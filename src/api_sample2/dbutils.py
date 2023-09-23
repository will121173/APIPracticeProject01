import sqlite3

def InsertRecord(con,recordData):
    cur = con.cursor()
    sql = "INSERT INTO Records(Price, ItemName, AccountingDate, CreateUserId) VALUES(?,?,?,?);"
    cur.execute(sql,recordData)
    con.commit()

def InsertUser(con,userData):
    cur = con.cursor()
    sql = "INSERT INTO Users(UserName) VALUES(?);"
    cur.execute(sql,userData)
    con.commit()
    

# あるユーザーの全データを表示
def SelectRecordsFromUserId(con,userId=None):
    cur = con.cursor()
    if userId is None:
        # デバッグ用　全データ表示
        sql = "Select Price, ItemName, AccountingDate, UserName from Records left join Users on CreateUserId=Users.Id;"
        return cur.execute(sql).fetchall()
    else:
        sql = "Select Price, ItemName, AccountingDate, UserName from Records left join Users on CreateUserId=Users.Id Where CreateUserId=?;"
        return cur.execute(sql,(userId,)).fetchall()

if __name__ == '__main__':
    con = sqlite3.connect("sample2.db")
    InsertUser(con,('sample user',))
    InsertRecord(con,(100,"sample1","2000-01-01",1))
    InsertRecord(con,(200,"sample2","2000-01-02",1))
    cur = con.cursor()
    print(cur.execute("select * from Records;").fetchall())
    print(cur.execute("select * from Users;").fetchall())
    con.close()



