from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.post import Post
from schemas.post import PostCreate, PostUpdate

def create_post(db: Session, post_data: PostCreate):
    new_post = Post(**post_data.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_posts(db: Session):
    return db.query(Post).all()

def get_post_detail(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
    return post

def update_post(db: Session, post_id: int, update_data: PostUpdate):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
    
    post.title = update_data.title
    post.content = update_data.content
    db.commit()
    db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
    
    db.delete(post)
    db.commit()
    return post