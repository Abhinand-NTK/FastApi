from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/",deprecated=True,description="This is the first route")
async def root():
    return {"message":"Hello World"}

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

@app.post("/")
def post():
    return {"message":"Hello world I am ready to post something"}

@app.put("/")
def put():
    return {"message":"Hello world I am ready to edit something"}