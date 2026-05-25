from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.comment import Comment  # 프로젝트 구조에 맞게 임포트 경로 확인 필요
from schemas.comment import CommentCreate, CommentUpdate

def create_comment(db: Session, post_id: int, comment_data: CommentCreate):
    # 특정 게시글에 종속되므로 post_id를 함께 넣어줍니다.
    new_comment = Comment(**comment_data.model_dump(), post_id=post_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_comments_by_post(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()

def update_comment(db: Session, comment_id: int, update_data: CommentUpdate):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail=f"{comment_id}번 댓글을 찾을 수 없습니다.")
    
    comment.content = update_data.content
    db.commit()
    db.refresh(comment)
    return comment

def delete_comment(db: Session, comment_id: int):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail=f"{comment_id}번 댓글을 찾을 수 없습니다.")
    
    db.delete(comment)
    db.commit()
    return comment