
# 사용법

## 1) FastAPI

### 1. 가상환경 생성 및 활성화
```bash
python3 -m venv .venv 
source .venv/bin/activate

```

### 2. FastAPI 및 실행 라이브러리 설치

```bash
pip install fastapi[standard] 

```

### 3. FastAPI 서버 실행

```bash
fastapi dev

```

---

# 실행 예시

## 1) API EndPoint

### 게시글(Posts)

| 메서드 | 경로 | 설명 |
| --- | --- | --- |
| POST | /posts | 게시글 생성 |
| GET | /posts | 게시글 조회 |
| GET | /posts/{post_id} | 특정 게시글 조회 |
| PATCH | /posts/{post_id} | 특정 게시글 수정 |
| DELETE | /posts/{post_id} | 특정 게시글 삭제 |

### 댓글(Comments)

| 메서드 | 경로 | 설명 |
| --- | --- | --- |
| POST | /posts/{post_id}/comments | 댓글 생성 |
| GET | /posts/{post_id}/comments | 댓글 조회 |
| PATCH | /posts/{post_id}/comments/{comment_id} | 특정 댓글 수정 |
| DELETE | /posts/{post_id}/comments/{comment_id} | 특정 댓글 삭제 |

### AI 요약(Summary)

| 메서드 | 경로 | 설명 |
| --- | --- | --- |
| POST | /posts/{post_id}/summaries | 특정 게시글 요약 생성 |

## 2} swagger

---

# 파일 구조

```text
│
├── core/
│   ├── config.py          # 환경 변수 및 글로벌 설정
│   └── database.py        # SQLAlchemy 엔진 및 세션 관리
│
├── models/                # 데이터베이스 은유 계층 (SQLAlchemy ORM)
│   ├── post.py
│   ├── comment.py
│   └── summary.py
│
├── schemas/               # 데이터 검증 계층 (Pydantic DTO)
│   ├── post.py
│   ├── comment.py
│   └── summary.py
│
├── routers/               # 엔드포인트 라우팅 계층 (Controller)
│   ├── posts.py
│   ├── comments.py
│   └── summaries.py
│
├── services/              # 비즈니스 로직 및 외부 연동 (Ollama 등)
│   └── ollama.py
│
└── main.py                # 애플리케이션 진입점 (App 초기화 & 미들웨어)

```

---

# 회고

FastAPI를 처음 사용해보면서

```

```