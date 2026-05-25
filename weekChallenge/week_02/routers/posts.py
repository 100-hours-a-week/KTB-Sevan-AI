from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.post import PostCreate, PostUpdate
# 모듈 통째로 가져와서 별칭 지정
import controllers.post as post_controller

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = post_controller.create_post(db, post)
    return {"message": "새로운 게시글을 생성하였습니다.", "data": new_post}


@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    posts = post_controller.get_posts(db)
    return {"message": "게시글을 조회하였습니다.", "data": posts}


@router.get("/{post_id}")
def get_post_detail(post_id: int, db: Session = Depends(get_db)):
    post = post_controller.get_post_detail(db, post_id)
    return {"message": "게시글을 조회하였습니다.", "data": post}


@router.patch("/{post_id}")
def update_post(post_id: int, update_data: PostUpdate, db: Session = Depends(get_db)):
    post = post_controller.update_post(db, post_id, update_data)
    return {"message": f"{post_id}번 게시글이 수정되었습니다.", "data": post}


@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post_controller.delete_post(db, post_id)
    return {"message": f"{post_id}번 게시글이 삭제되었습니다.", "data": None}# from fastapi import APIRouter, Depends, HTTPException, status





# from sqlalchemy.orm import Session
# from core.database import get_db
# from models.post import Post
# from schemas.post import PostCreate, PostUpdate

# router = APIRouter(prefix="/posts", tags=["Posts"])

# @router.post("/", status_code=status.HTTP_201_CREATED)
# # db: Session = Depends(get_db) db 연결(session) 하고 변수(db)에 꽂는다
# def create_post(post: PostCreate, db: Session = Depends(get_db)):
#     # 키=값 형태의 인자(Argument)로 풀어서 전달
#     new_post = Post(**post.model_dump())
#     # git add 처럼 스테이지에 올린다
#     db.add(new_post)
#     # git commit+push 처럼 db에 최종 저장한다
#     db.commit()
#     # db 새로고침
#     db.refresh(new_post)
#     return {"message": "새로운 게시글을 생성하였습니다.", "data": new_post}


# @router.get("/")
# def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(Post).all()
#     return {"message": "게시글을 조회하였습니다.", "data": posts}

# @router.get("/{post_id}")
# def get_post_detail(post_id: int, db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
#     return {"message": "게시글을 조회하였습니다.", "data": post}

# @router.patch("/{post_id}")
# def update_post(post_id: int, update_data: PostUpdate, db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
    
#     post.title = update_data.title
#     post.content = update_data.content
#     db.commit()
#     db.refresh(post)
#     return {"message": f"{post_id}번 게시글이 수정되었습니다.", "data": post}

# @router.delete("/{post_id}")
# def delete_post(post_id: int, db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
    
#     db.delete(post)
#     db.commit()
#     return {"message": f"{post_id}번 게시글이 삭제되었습니다.", "data": None}

