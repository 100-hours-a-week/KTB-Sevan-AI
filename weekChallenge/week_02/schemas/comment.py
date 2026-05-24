from pydantic import BaseModel, ConfigDict

class CommentBase(BaseModel):
    author: str
    content: str

class CommentCreate(CommentBase):
    pass

class CommentUpdate(BaseModel):
    content: str

class CommentResponse(CommentBase):
    id: int
    post_id: int

    model_config = ConfigDict(from_attributes=True)