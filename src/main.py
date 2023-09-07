from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

import datetime
@app.get("/date/",
    summary='date information ',
    description='年月日と平日か否かを出力する。forwardパラメータに入れた整数分だけ先の日付をしていできる・',
    response_description='response',
    tags=['sample']
    )
async def get_date(forward:int=0):
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    date = now.today() + datetime.timedelta(days=forward)
    return {
        "date": date.date(),
        "is_weekday" : "平日です" if date.isoweekday() else "休日です"
        }

