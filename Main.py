from typing import Optional

from pydantic import BaseModel
class Post (BaseModel):
    id: int
    title: str
    content: str
    likes: int = 0


from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/post")
def list_post():
    return posts

posts ={
    1: {"likes":0},
    2: {"likes":0}
}

user_likes ={}

# To like a post

@app.post ("/like/{post_id}")
def like_post (post_id: int, user_id: int):
    if post_id not in posts:
        raise HTTPException (status_code=404, detail ="Post not found")

    if (user_id, post_id) in user_likes:
        raise HTTPException(status_code=400, detail ="Post already liked")

    posts[post_id].likes +=1
    user_likes[(user_id,post_id)]= True
    return {"detail": "Post liked!"}


# To count likes

@app.get("/likes/{post_id}")
def like_count(post_id: int):
    if post_id not in posts:
        raise HTTPException (status_code=404, details="post not found")

    return{"post_id":post_id, "like_count": posts[post_id]["likes"]}

