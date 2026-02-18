from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data 

@app.get('/')
def hello():
    return {'message':'This is Patient Data Management System'}

@app.get('/view')
def view_data():
    data = load_data()
    return data


@app.get('/patients/{patient_id}')
def patient(patient_id : str = Path(..., description='Enter a patient id in the DB', examples='P001')):
    data = load_data()

    if patient_id  in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')


@app.get('/sort')
def sort(sort_by : str =Query(...,description="Sort by bmi, hieght or wieght"), order : str = Query('asc', description=('Sort in asc or desc oreder'))):

    valid_fields = ['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Add a valid field from following fields : {valid_fields}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, description= "Add a valid order from asc or desc")
    
    data = load_data()
    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data