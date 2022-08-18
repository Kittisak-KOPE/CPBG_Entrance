from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from db_pq import databasepq

app = FastAPI()

app.mount("/dataImage", StaticFiles(directory="dataImage"), name="dataImage")

@app.get("/", response_class=HTMLResponse)
def index():
    with open("test.html", "r", encoding='utf-8') as f:
        html = f.read()
    return html


@app.get("/api")
def api():
    db = databasepq(
        host = 'localhost',
        database = 'sp_parking',
        user = 'postgres',
        password = 'postgres',
        port = 5432
    )

    query_script = f"SELECT * FROM parkingdata ORDER BY id ASC "

    db.query(query_script)
    rows = db.fetchAll()
    array= []
    for row in rows:
        array.append({
            "id":row[0],
            "card_id":row[1],
            "data_cam":row[2],
            "data_date":row[3],
        })
    db.close()
    return array