from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World <3"}

@app.get("/posts")
def get_posts():
    return {"data": [{"name":"mihai"}, {"name":"Catalina"}]}