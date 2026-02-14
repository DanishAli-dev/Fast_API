from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message" : "Welcome to my first FAST API app"}


@app.get("/about")
def about():
    return {
        "Name" : "Danish Ali",
        "Role" : "AI Engineer"
    }