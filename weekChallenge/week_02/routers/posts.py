from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from models.post import Post
from schemas.post import PostCreate, PostUpdate

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message": "새로운 게시글을 생성하였습니다.", "data": new_post}

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return {"message": "게시글을 조회하였습니다.", "data": posts}

@router.get("/{post_id}")
def get_post_detail(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
    return {"message": "게시글을 조회하였습니다.", "data": post}

@router.patch("/{post_id}")
def update_post(post_id: int, update_data: PostUpdate, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
    
    post.title = update_data.title
    post.content = update_data.content
    db.commit()
    db.refresh(post)
    return {"message": f"{post_id}번 게시글이 수정되었습니다.", "data": post}

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
    
    db.delete(post)
    db.commit()
    return {"message": f"{post_id}번 게시글이 삭제되었습니다.", "data": None}