from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from core.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    # String 뒤에 길이를 명시합니다 (예: 255글자 제한)
    title = Column(String(255), index=True) 
    content = Column(Text)
    author = Column(String(255)) # String 길이를 명시합니다.

    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
    summary = relationship("Summary", back_populates="post", uselist=False, cascade="all, delete-orphan")