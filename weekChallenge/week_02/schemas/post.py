from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from schemas.comment import CommentResponse
from schemas.summary import SummaryResponse

class PostBase(BaseModel):
    title: str
    content: str
    author: str

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: str
    content: str

class PostListResponse(PostBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    
class PostResponse(PostBase):
    id: int
    # 게시글에 달린 댓글/요약을 묶어서 가져오기 위해 이 정보를 가져온다.
    # 그렇게 하지 않으면 api를 두 번 호출해야 되어서 비효율적이다.
    comments: List[CommentResponse] = []
    summary: Optional[SummaryResponse] = None

    #ORM(Object-Relational Mapping) 객체를 Pydantic 모델로 자동 변환
    model_config = ConfigDict(from_attributes=True)