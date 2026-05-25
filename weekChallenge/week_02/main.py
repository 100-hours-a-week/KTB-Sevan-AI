from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Database 및 Models
from core.database import engine, Base
# from models import post, comment, summary 

# Routers
from routers import posts, comments, summaries

# 앱 실행 시 DB 테이블 자동 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(summaries.router)







# from fastapi import FastAPI, status, HTTPException
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from ollama_client import request_ollama



# app = FastAPI()
# # fastapi를 생성한다


# # 미들웨어 설정
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],  # GET, POST, PUT, DELETE 전부 허용
#     allow_headers=["*"],
# )


# # 게시글 생성
# class Post(BaseModel):
#   title: str
#   content: str
# #   id: int
# #  id는 어차피 서버가 매기니까 제외해도 됨
#   author: str


# # 게시글 수정
# class PostUpdate(BaseModel):
#   title: str
#   content: str


# # 댓글 달기
# class CreateComment(BaseModel):
#   author: str
#   content: str

# # 댓글 수정
# class CommentUpdate(BaseModel):
#   content: str



# # 게시글 요약
# # class PostSummary(BaseModel):
# #   content: str
# # 인자로 받는게 아니라 ollama파일의 함수 리턴값으로 받아라



# posts = list()
# current_post_id = 0

# # ----------------------------------------------------
# # 게시글 생성 (POST)
# # ----------------------------------------------------
# # 생성이면 200 대신 201 인 status를 명시한다.
# @app.post("/posts/", status_code=status.HTTP_201_CREATED)
# # 데코레이터를 활용해 필요한 연결 기능을 가져온다
# def create_post(post: Post):
#    global current_post_id
#    current_post_id +=1

#    new_post = {
#      "id": current_post_id,
#      "title":  post.title,
#      "content": post.content,
#      "author": post.author,
#      "comments": [],
#      "last_comment_id": 0,
#      "summaries": ""

#    }

# # ("comment": post.comment): * 글을 쓸 때 무조건 댓글 내용을 같이 채워서 올려야만 하는 오류가 생깁니다. (나중에 댓글이 여러 개 달릴 수도 없어서 게시판 기능이 망가집니다.)
# # ("comments": [])

#    posts.append(new_post)
#    return {"message": f"새로운 게시글을 생성하였습니다." , "data":posts}

# # ----------------------------------------------------
# # 게시글 전체 조회 (GET)
# # ----------------------------------------------------
# @app.get("/posts/")
# def get_posts():
#   return {"message": f"게시글을 조회하였습니다." , "data":posts}


# # ----------------------------------------------------
# # 특정 게시글 조회 (GET)
# # ----------------------------------------------------
# @app.get("/posts/{post_id}")
# def get_post_detail(post_id: int):
#   for post in posts:
#     if post["id"] == post_id:
#       return {"message": f"게시글을 조회하였습니다." , "data":post}
#   raise HTTPException (status_code =404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")

# # ----------------------------------------------------
# # 게시글 수정 (PATHCH)
# # ----------------------------------------------------
# @app.patch("/posts/{post_id}")
# def update_posts(post_id: int, update_post:PostUpdate):
#   for post in posts:
#     if post["id"] == post_id:
#         post["title"] = update_post.title
#         post["content"] = update_post.content

#         return {"message": f"{post_id}번 게시글이 수정되었습니다." , "data": post}

#   raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")


# # ----------------------------------------------------
# # 게시글 삭제 (DELETE)
# # ----------------------------------------------------

# @app.delete("/posts/{post_id}")
# def delete_posts(post_id: int):
#   for post in posts:
#     if post["id"] == post_id:
#        posts.remove(post)
#        return {"message": f"{post_id}번 게시글이 삭제되었습니다.", "data": None}
    
#   raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")


# # ----------------------------------------------------
# # 댓글 생성 (POST)
# # ----------------------------------------------------

# @app.post("/posts/{post_id}/comments")
# def create_comments(post_id: int, create_comment: CreateComment):
#   for post in posts:
#     if post["id"] == post_id:
#       post["last_comment_id"] += 1
#       new_comment = {
#         "id": post["last_comment_id"],
#         "author": create_comment.author,
#         "content": create_comment.content
# 	  }
#       post["comments"].append(new_comment)
#       return {"message": f"{post_id}에 댓글이 성공적으로 달렸습니다.", "data": new_comment}
      
#   raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")



# # ----------------------------------------------------
# # 댓글 조회 (GET)
# # ----------------------------------------------------
# @app.get("/posts/{post_id}/comments/{comment_id}")
# def get_comments(post_id: int, comment_id : int ):
#   for post in posts:
#     if post["id"] == post_id:
#       # comments 는 어디에 있을끼 ? -> post 안에 존재하므로 post["comments"]를 가져와야 한다!
#       for comment in post["comments"]:
#         if comment["id"] == comment_id:
#           return {"message": f"{comment_id}번 댓글을 조회하였습니다."}
#       raise HTTPException(status_code=404, detail =f"{comment_id}번 댓글을 찾을 수 없습니다.")
#     raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")    

# # ----------------------------------------------------
# # 댓글 수정(PATCH)
# # ----------------------------------------------------
# @app.patch("/posts/{post_id}/comments/{comment_id}")
# def update_comments(post_id: int, comment_id: int, update_comment: CommentUpdate):
#     for post in posts:
#         if post["id"] == post_id:
#             for comment in post["comments"]:
#                 if comment["id"] == comment_id:
#                   # 댓글 content만 변경하는 것이므로 update_commet.comment라고 해주어야 한다.
#                   comment["content"] = update_comment.content
#                   return {"message": f"{comment_id}번 댓글을 수정하였습니다."}
#             raise HTTPException(status_code=404, detail =f"{comment_id}번 댓글을 찾을 수 없습니다.")
#     raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")    


# # ----------------------------------------------------
# # 댓글 삭제(DELETE)
# # ----------------------------------------------------
# @app.delete("/posts/{post_id}/comments/{comment_id}")
# def delete_comment(post_id: int, comment_id: int):
#     for post in posts:
#         if post["id"] == post_id:
#             for comment in post["comments"]:
#                 if comment["id"] == comment_id:
#                     post["comments"].remove(comment)
#                     return {"message": f"{comment_id}번 댓글이 삭제되었습니다.", "data": None}
#             raise HTTPException(status_code=404, detail=f"{comment_id}번 댓글을 찾을 수 없습니다.")
#     raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")


# # ----------------------------------------------------
# # 특정 게시글 요약 생성 (POST)
# # ----------------------------------------------------

# @app.post("/posts/{post_id}/summaries")
# def ai_summaries(post_id: int):
#   for post in posts:
#     if post["id"] == post_id:
#       # ollama_client.py 에서 request_ollama 함수를 불러온다. 그리고 게시글의 content를 인자로 넣어준다. 리턴값을 여기에 가져온다.
#       ai_summary = request_ollama(post["content"])
#       post["summaries"] = ai_summary
#       return {"message": f"{post_id}에 AI요약이 성공적으로 만들어졌습니다.", "data": ai_summary}
#   raise HTTPException(status_code=404, detail=f"{post_id}번 게시글을 찾을 수 없습니다.")






