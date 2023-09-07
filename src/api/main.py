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
    description='年月日と平日か否かを出力する。forwardパラメータに入れた整数分だけ先の日付をしていできる・',
    response_description='response',
    tags=['sample']
    )    
async def get_date(forward:int=0):
    nowDatetime = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    targetDatetime = nowDatetime.today() + datetime.timedelta(days=forward)
    return {
        "date": targetDatetime.date(),
        "is_weekday" : "平日です" if targetDatetime.isoweekday() else "休日です"
        }

