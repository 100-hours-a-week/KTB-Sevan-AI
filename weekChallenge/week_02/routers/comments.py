from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.comment import CommentCreate, CommentUpdate
import controllers.comment as comment_controller

# router = APIRouter(prefix="", tags=["Comments"])
router = APIRouter(prefix="/posts/{post_id}/comments", tags=["Comments"])

# 특정 게시글에 댓글 작성
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_comment(post_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    new_comment = comment_controller.create_comment(db, post_id, comment)
    return {"message": "댓글이 등록되었습니다.", "data": new_comment}

# 특정 게시글의 모든 댓글 조회
@router.get("/{comment_id}")
def get_comments(post_id: int, db: Session = Depends(get_db)):
    comments = comment_controller.get_comments_by_post(db, post_id)
    return {"message": "댓글 목록을 조회하였습니다.", "data": comments}

# 댓글 수정
@router.patch("/{comment_id}")
def update_comment(comment_id: int, update_data: CommentUpdate, db: Session = Depends(get_db)):
    comment = comment_controller.update_comment(db, comment_id, update_data)
    return {"message": f"{comment_id}번 댓글이 수정되었습니다.", "data": comment}

# 댓글 삭제
@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    comment_controller.delete_comment(db, comment_id)
    return {"message": f"{comment_id}번 댓글이 삭제되었습니다.", "data": None}





# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from core.database import get_db
# from models.post import Post
# from models.comment import Comment
# from schemas.comment import CommentCreate, CommentUpdate

# router = APIRouter(prefix="/posts/{post_id}/comments", tags=["Comments"])

# @router.post("/")
# def create_comment(post_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
#     # 키=값 형태의 인자(Argument)로 풀어서 전달
#     new_comment = Comment(**comment.model_dump(), post_id=post_id)
#     db.add(new_comment)
#     db.commit()
#     db.refresh(new_comment)
#     return {"message": f"{post_id}에 댓글이 성공적으로 달렸습니다.", "data": new_comment}

# @router.get("/{comment_id}")
# def get_comment(post_id: int, comment_id: int, db: Session = Depends(get_db)):
#     # first() -> 처음 데이터만 가져온다
#     # models/comment.py에 있는 Comment의 id , post_id를 비교한다
#     comment = db.query(Comment).filter(Comment.id == comment_id, Comment.post_id == post_id).first()
#     if not comment:
#         raise HTTPException(status_code=404, detail=f"{comment_id}번 댓글을 찾을 수 없습니다.")
#     return {"message": f"{comment_id}번 댓글을 조회하였습니다.", "data": comment}

# @router.patch("/{comment_id}")
# def update_comment(post_id: int, comment_id: int, update_data: CommentUpdate, db: Session = Depends(get_db)):
#     comment = db.query(Comment).filter(Comment.id == comment_id, Comment.post_id == post_id).first()
#     if not comment:
#         raise HTTPException(status_code=404, detail=f"{comment_id}번 댓글을 찾을 수 없습니다.")
    
#     comment.content = update_data.content
#     db.commit()
#     db.refresh(comment)
#     return {"message": f"{comment_id}번 댓글을 수정하였습니다.", "data": comment}

# @router.delete("/{comment_id}")
# def delete_comment(post_id: int, comment_id: int, db: Session = Depends(get_db)):
#     comment = db.query(Comment).filter(Comment.id == comment_id, Comment.post_id == post_id).first()
#     if not comment:
#         raise HTTPException(status_code=404, detail=f"{comment_id}번 댓글을 찾을 수 없습니다.")
    
#     db.delete(comment)
#     db.commit()
#     return {"message": f"{comment_id}번 댓글이 삭제되었습니다.", "data": None}

