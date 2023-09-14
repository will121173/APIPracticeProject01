from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

import datetime
@app.get("/date/",
    summary='date and weekday information',
    description='実行した年月日と平日か否かを出力する。forwardパラメータに整数を入れるとその数だけ先の日付で判定する。',
    response_description='response',
    tags=['sample']
    )    
async def get_date(forward:int=0):
    nowDatetime = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    targetDatetime = nowDatetime.today() + datetime.timedelta(days=forward)
    return {
        "date": targetDatetime.date(),
        "is_weekday" : "平日です" if targetDatetime.isoweekday()>5 else "休日です"
        }

