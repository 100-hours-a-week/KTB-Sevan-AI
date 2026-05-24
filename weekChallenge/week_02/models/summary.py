from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Summary(Base):
    __tablename__ = "summaries"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"), unique=True)
    content = Column(Text)

    post = relationship("Post", back_populates="summary")