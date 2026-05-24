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

class PostResponse(PostBase):
    id: int
    comments: List[CommentResponse] = []
    summary: Optional[SummaryResponse] = None

    model_config = ConfigDict(from_attributes=True)