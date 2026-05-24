from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models.post import Post
from models.summary import Summary
from services.ollama import request_ollama

router = APIRouter(prefix="/posts/{post_id}/summaries", tags=["Summaries"])

@router.post("/")
def ai_summaries(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
    
    # ollama 함수 리턴값을 받아 DB에 저장
    ai_summary_text = request_ollama(post.content)

    if post.summary:
        post.summary.content = ai_summary_text
    else:
        new_summary = Summary(post_id=post_id, content=ai_summary_text)
        db.add(new_summary)
    
    db.commit()
    return {"message": f"{post_id}에 AI요약이 성공적으로 만들어졌습니다.", "data": ai_summary_text}