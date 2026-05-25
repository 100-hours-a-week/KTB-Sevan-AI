from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from core.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True) 
    content = Column(Text)
    author = Column(String(255)) 
    
    # 일대다관계
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    # 일대일관계
    summary = relationship("Summary", back_populates="post", uselist=False, cascade="all, delete-orphan")
