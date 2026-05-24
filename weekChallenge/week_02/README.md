# 웹 백엔드 핵심 요약 가이드 (HTTP & FastAPI)

본 문서는 HTTP 통신 프로토콜의 기초 개념과 구조, 그리고 FastAPI 프레임워크를 활용한 효율적인 Request Body 검증 및 아키텍처 설계 방법을 정리한 개발 가이드북입니다.

---

## 1. HTTP (HyperText Transfer Protocol) 개요

### 1.1 HTTP 정의 및 사용 목적
* **정의**: HTML, 이미지, 비디오 등 다양한 파일과 텍스트 데이터를 전송하기 위해 클라이언트와 서버 간에 사용하는 상호 간의 통신 규칙이자 약속입니다.
* **사용 목적**: 웹 페이지 간의 유연한 이동을 지원하고, 분산된 시스템 환경에서 정보를 신뢰성 있게 전송하며 연결하기 위함입니다.

### 1.2 HTTP 메시지 구조
클라이언트(브라우저)와 서버가 데이터를 주고받는 기본 단위이며, 크게 네 가지 요소로 구성됩니다.
1. **시작줄 (Start Line)**: 요청(Request) 시에는 `Method + URL + HTTP Version`이 들어가며, 응답(Response) 시에는 `HTTP Version + Status Code + Status Message`가 포함됩니다.
2. **헤더 (Headers)**: 메시지 본문에 대한 메타데이터 정보를 포함합니다.
3. **빈 줄 (Empty Line)**: 헤더의 끝과 본문의 시작을 물리적으로 구분하는 공백 라인입니다.
4. **본문 (Body)**: 실제 전송하고자 하는 데이터(JSON, HTML, 파일 등)가 위치합니다.

### 1.3 HTTP의 주요 특성: 무상태성 (Stateless)
* **개념**: 서버는 클라이언트의 과거 요청 상태를 내부적으로 저장하거나 유지하지 않습니다.
* **영향**: 각 요청은 독립적으로 처리되므로, 인증이 필요한 API의 경우 매 요청마다 인증 정보(예: JWT 토큰)나 필수 컨텍스트를 헤더 또는 요청 데이터에 포함하여 함께 전송해야 합니다.

---

## 2. HTTP Method & Status Code

### 2.1 HTTP Method (행위의 정의)
URL은 관리하고자 하는 대상 자원(Resource)만을 지칭하며, 해당 자원에 대한 구체적인 행위는 HTTP Method를 통해 엄격히 구분합니다.

| Method | 행위 | 주요 목적 | 비고 |
| :--- | :--- | :--- | :--- |
| **GET** | 조회 (Read) | 특정 자원의 상세 정보나 목록을 가져옴 | Body를 포함하지 않는 것이 원칙 |
| **POST** | 생성 (Create) | 시스템에 새로운 자원을 등록함 | AI 추론 요청, 회원가입 등에 활용 |
| **PUT/PATCH**| 수정 (Update) | 자원의 전체(PUT) 또는 일부(PATCH) 내용을 변경 | 데이터 정밀 수정 시 PATCH 권장 |
| **DELETE** | 삭제 (Delete) | 특정 자원을 시스템에서 제거 | 삭제 성공 여부를 상태 코드로 반환 |

### 2.2 HTTP Status Code (응답 상태 코드)
서버가 클라이언트의 요청을 처리한 결과를 3자리 숫자로 명확하게 분류하여 알려줍니다.

* **1xx (Informational)**: 요청을 받았으며 작업을 진행 중임을 나타내는 정보 메시지
* **2xx (Successful)**: 요청이 성공적으로 처리됨
  * `200 OK`: 요청 성공 및 결과 반환
  * `201 Created`: 자원 생성 성공 (POST 요청에 대한 주된 응답)
* **3xx (Redirection)**: 요청을 완료하기 위해 클라이언트의 추가적인 주소 이동(리다이렉션)이 필요함
* **4xx (Client Error)**: 클라이언트의 요청에 잘못된 부분이 있어 서버가 처리를 거부함
  * `400 Bad Request`: 요청 파라미터나 구조가 잘못됨
  * `401 Unauthorized`: 인증 자격 증명이 누락되었거나 유효하지 않음
  * `404 Not Found`: 요청한 URL 또는 자원이 존재하지 않음
* **5xx (Server Error)**: 클라이언트의 요청은 유효했으나, 백엔드 코드 내부 에러로 인해 처리에 실패함
  * `500 Internal Server Error`: 서버 내부 런타임 예외 발생 (서버 크래시 등)

---

## 3. HTTP Header 상세

### 3.1 요청 헤더 (Request Header)
* **역할**: 클라이언트 자체의 환경 정보와 요청의 성격, 목적을 전달합니다.
* **예시**: `User-Agent` (브라우저/OS 정보), `Authorization` (인증 토큰).

### 3.2 응답 헤더 (Response Header)
* **역할**: 서버의 정보 및 클라이언트가 응답 데이터를 어떻게 처리하고 렌더링해야 하는지에 대한 가이드를 제공합니다.
* **주요 필드**:
  * `Server`: 웹 서버의 소프트웨어 및 버전 정보
  * `Age`: 캐싱 프록시 서버에서 응답이 캐시된 후 지난 시간(초 단위)
  * `X-Cache-Info`: 캐싱 프록시 서버가 해당 요청을 어떻게 처리했는지에 대한 동작 기록

### 3.3 일반 헤더 (General Header)
* **역할**: 요청/응답 메시지 전체에 공통으로 적용되는 일반적인 메타데이터입니다.
* **예시**: `Connection` (연결 유지 여부), `Cache-Control` (캐싱 지침).

### 3.4 대표 헤더 (Entity Header / Content Header)
* **역할**: 메시지 본문(Body)의 데이터와 직접적으로 관련된 서식 및 특징을 나타냅니다.
* **주요 필드**:
  * `Content-Type`: 본문 데이터의 유형 및 인코딩 방식 (예: `application/json; charset=utf-8`)
* **특이사항**: 서버는 데이터 유효성 검증 시 이 헤더를 참고하여 요청 본문의 크기가 비정상적으로 길거나 짧을 경우 내부 로직 진입 전에 요청을 거절(Reject)할 수 있습니다.

---

## 4. FastAPI에서 Request Body 검증하기

### 4.1 검증이 필수적인 이유
1. **예상치 못한 서버 에러(Crash) 방지**
   * 외부 클라이언트가 보내는 데이터는 언제나 유실되거나 형태가 뒤틀릴 수 있습니다.
   * 예를 들어, 정수형(`int`) 데이터가 들어와야 하는 `age` 필드에 `"스물다섯"`과 같은 문자열이 유입될 때 이를 검증 없이 수용하면, 비즈니스 로직이나 DB 적재 단계에서 런타임 에러가 발생해 서버가 중단될 수 있습니다.
   * API 진입부에서 데이터의 '형태와 타입'을 완벽히 필터링해주면, 핵심 비즈니스 로직 코드를 작성할 때 데이터의 무결성을 신뢰하고 깔끔한 코드를 유지할 수 있습니다.
2. **보안 및 데이터 무결성 보장**
   * 입력값의 타입을 맞추는 것을 넘어, 악의적이거나 비정상적인 범위의 값을 선제 차단해야 합니다.
   * 비밀번호의 최소 길이 미달, 비현실적인 나이 입력(예: 500세), 이메일 형식 미준수 데이터가 DB 레이어까지 흘러 들어가는 것을 막습니다.
   * 클라이언트가 허용되지 않은 필드(예: `is_admin: true`)를 임의로 주입하더라도, 지정된 Pydantic 모델(DTO) 외의 필드는 자동으로 무시하므로 안전합니다.
3. **자동 문서화를 통한 협업 효율화**
   * FastAPI는 코드 내 선언된 Pydantic 모델을 해석하여 대화형 API 문서인 `/docs` (Swagger UI)를 실시간으로 자동 생성합니다.
   * 개발자가 명세서를 수동으로 갱신할 필요 없이, 검증 제약 조건이 문서에 즉시 반영되므로 프론트엔드 개발자와의 소통 비용이 획기적으로 절감됩니다.

> 💡 **한 줄 요약**: 악성 데이터가 시스템 내부에 진입하여 문제를 일으키기 전, 백엔드의 최전방 대문에서 자동으로 출입을 통제하는 보안관을 배치하는 작업입니다.

### 4.2 Pydantic을 활용한 검증 구현 예시

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class UserRegisterSchema(BaseModel):
    # 1. 문자열 길이 제한 (최소 3자, 최대 20자)
    username: str = Field(min_length=3, max_length=20, description="사용자 아이디")
    
    # 2. 정규식(Regex)을 이용한 비밀번호 검증 (소문자, 숫자 포함 8자 이상)
    password: str = Field(pattern=r"^(?=.*[a-z])(?=.*\d).{8,}$", description="비밀번호")
    
    # 3. EmailStr을 통한 이메일 형식 자동 검증
    email: EmailStr
    
    # 4. 숫자 범위 제한 (최소 1세, 최대 120세)
    age: int = Field(ge=1, le=120, description="나이")
    
    # 5. 기본값(Default) 설정 및 Optional 필드 구성 (Union Type 활용)
    bio: str | None = Field(default=None, max_length=500, description="자기소개(선택)")

@app.post("/users/signup", status_code=201)
def signup(user_data: UserRegisterSchema):
    # 본 엔드포인트 함수 내부로 진입했다는 것은 데이터가 위 유효성 조건을 완벽히 통과했음을 보장합니다.
    return {
        "status": "success",
        "registered_user": user_data.username
    }
5. 실전 API 엔드포인트 설계 예시
자원(Resource) 중심의 RESTful 원칙에 맞추어 설계된 게시글, 댓글 및 AI 요약 API 명세 구조입니다.

5.1 게시글 (Posts) API
POST /posts: 게시글 생성

GET /posts: 게시글 전체 목록 또는 필터링 조회

GET /posts/{post_id}: 특정 ID를 가진 게시글의 상세 정보 조회

PATCH /posts/{post_id}: 특정 게시글의 일부 필드 수정

DELETE /posts/{post_id}: 특정 게시글 완전 삭제

5.2 댓글 (Comments) API
POST /posts/{post_id}/comments: 특정 게시글 하위에 새로운 댓글 생성

GET /posts/{post_id}/comments: 특정 게시글에 종속된 댓글 목록 조회

PATCH /posts/{post_id}/comments/{comment_id}: 특정 댓글 내용 수정

DELETE /posts/{post_id}/comments/{comment_id}: 특정 댓글 삭제

5.3 AI 요약 (Summary) API
POST /posts/{post_id}/summaries: Ollama 등의 LLM 서비스를 연동하여 특정 게시글의 텍스트 내용을 요약한 데이터 생성 요청

6. 프로덕션 레벨 아키텍처 및 파일 구조
관심사 분리(Separation of Concerns) 원칙을 준수하여 각 레이어의 역할과 책임을 명확히 분리한 구조입니다. 이렇게 설계함으로써 대규모 프로젝트에서도 코드의 가독성, 유지보수성 및 확장성을 확보할 수 있습니다.

Plaintext
├── core/
│   ├── config.py          # 환경 변수(Dotenv), 글로벌 프로젝트 설정 관리
│   └── database.py        # SQLAlchemy 데이터베이스 엔진 생성 및 DB 세션(SessionLocal) 관리
│
├── models/                # 데이터베이스 은유 계층 (SQLAlchemy ORM)
│   ├── post.py            # posts 테이블 스키마 매핑 및 관계 정의
│   ├── comment.py         # comments 테이블 스키마 매핑
│   └── summary.py         # summaries 테이블 스키마 매핑
│
├── schemas/               # 데이터 검증 및 전송 계층 (Pydantic DTO)
│   ├── post.py            # 게시글 생성/수정/응답용 Pydantic 모델
│   ├── comment.py         # 댓글 유효성 검증 모델
│   └── summary.py         # AI 요약 결과 검증 모델
│
├── routers/               # 엔드포인트 라우팅 계층 (Controller)
│   ├── posts.py           # 게시글 관련 HTTP 요청 매핑 및 응답 반환
│   ├── comments.py        # 댓글 관련 API 경로 처리
│   └── summaries.py       # AI 요약 API 경로 처리
│
├── services/              # 비즈니스 핵심 로직 및 외부 컴포넌트 연동 계층
│   └── ollama.py          # 온디맨드(On-demand) 방식의 LLM API 호출 및 텍스트 요약 비즈니스 로직
│
└── main.py                # 애플리케이션 진입점 (FastAPI 인스턴스 초기화, 미들웨어 등록 및 라우터 통합)
7. 프로젝트 회고 (Retrospective)