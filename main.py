from typing import Optional

from fastapi import FastAPI, Response, status
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title":"post 1", "content":"content of post 1", "id":1},
    {"title":"post 2", "content":"content of post 2", "id":2},
]
@app.get("/")
async def root():
    return {"message": "Hello World <3"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/latestposts")
def get_latest_posts():
    return {"data": my_posts[len(my_posts) - 1]}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    print(id)
    found_post = None
    for post in my_posts:
        print(post["id"])
        if post["id"] == id:
            print(post)
            found_post = post
            break
    if not found_post:
        response.status_code = status.HTTP_404_NOT_FOUND
    return response

@app.post("/posts")
def create_post(post: Post, response: Response):
    new_post = post.dict()
    new_post["id"] = len(my_posts) + 1
    my_posts.append(new_post)
    response.status_code = status.HTTP_201_CREATED
    return {"new post":new_post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    for i in range(0, len(my_posts)):
        if my_posts[i]["id"] == id:
            print(my_posts[i]["id"])
            del my_posts[i]
            break
    return {"message":"deleted"}

