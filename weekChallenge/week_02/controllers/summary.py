from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.post import Post
from models.summary import Summary
from services.ollama import request_ollama

def create_or_update_ai_summary(db: Session, post_id: int) -> str:
    # 1. 게시글 존재 여부 확인
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")
    
    # 2. Ollama를 통해 요약문 생성
    ai_summary_text = request_ollama(post.content)

    # 3. 1:1 관계(post.summary)를 활용한 저장 및 갱신
    if post.summary:
        post.summary.content = ai_summary_text
    else:
        new_summary = Summary(post_id=post_id, content=ai_summary_text)
        db.add(new_summary)
    
    db.commit()
    
    # 생성된 텍스트를 리턴하여 라우터에서 쓸 수 있게 합니다.
    return ai_summary_text