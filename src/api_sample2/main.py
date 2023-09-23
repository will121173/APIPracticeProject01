from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dbutils import *

import sqlite3
# データベース sample2.db への接続
con = sqlite3.connect("sample2.db")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/",
    summary='root',
    description='動作確認用、トップページにただアクセスしたときは固定の文字を返す',
    )
async def root():
    return {"message": "Hello Sample-2"}


@app.get("/records/",
    summary='Show Records',
    description="""
    ユーザーIDを指定してレコードを表示する。認証を実装していないので誰でも見られる。<br>
    パラメータを省略すると全データ表示。
    """,)
async def get_records_from_userid(userid:int=None):
    records = SelectRecordsFromUserId(con,userid)
    return records

# POSTでボディを受け取るためのクラス
from pydantic import BaseModel
class RecordModel(BaseModel):
    price: int
    itemName: str
    accountingDate: str
    userId: int

@app.post("/records/",
    summary='Create Records',
    description='レコードを作成する。認証を実装していないので誰でも作れる<br>返り値なし',
    )
async def create_record(recordData : RecordModel):
    InsertRecord(con,(recordData.price,recordData.itemName,recordData.accountingDate,recordData.userId))
