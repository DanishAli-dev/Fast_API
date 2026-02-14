from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/")
def project():
    return {'message': "Patients Record Management System"}

@app.get("/about")
def about():
    return{'message':"This programme holds records of the patients."}

@app.get("/view")
def view_data():
    data = load_data()

    return data