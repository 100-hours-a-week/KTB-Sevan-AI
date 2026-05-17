# 🐱 LinkCat: URL 분류 및 관리 프로그램

**LinkCat**은 터미널 환경에서 웹사이트 링크(URL)를 카테고리별로 분류하여 저장하고, 필요할 때마다 카테고리별로 빠르게 조회할 수 있는 파이썬 기반의 CLI(Command Line Interface) 북마크 관리 도구입니다.

---

### 주제 선정 및 기초 구현

* **주제 선정 배경:** 
- url로 사람들이 관련 정보(꿀팁, 맛집, 행사)를 저장하거나 수집하긴 하는데 실제로 다시 열어보지 않는다.
- 중구난방으로 저장되어 내가 원하는 정보를 찾기 어렵다.
- 자동으로 카테고리 별로 저장되고 원할 때 꺼내볼 수 있었으면 좋겠다.

* **기초 구현 방식:** `argparse` 모듈의 `subparsers` 기능을 활용했습니다. 명령어의 성격에 따라 `add`와 `list`로 분리하였습니다.

---

## 주요 기능

* **카테고리별 링크 저장 (`add`):** 유저가 입력한 URL과 카테고리를 매핑하여 저장합니다.

* **목록 조회 (`list`):** 카테고리를 지정하지 않으면 저장된 전체 목록을 카테고리별 등록 개수와 함께 출력하며, 특정 카테고리를 지정하면 해당 카테고리의 링크들만 필터링하여 보여줍니다.

---

## 사용 기술

* **Language:** Python 3.9.6
* **CLI Arguments Parsing:** `argparse` (Python 내장 모듈)
* **Data Storage & I/O:** `json`, `os` (Python 내장 모듈)

---

## 프로젝트 구조

```text
.
├── main.py       # 인터페이스 레이어 (CLI 명령어 라우팅 및 인자 파싱)
├── manager.py    # 데이터 레이어 (JSON 파일 생성, 로드, 데이터 저장 및 출력 로직)
└── links.json    # 영속성을 보장하는 키-값(Key-Value) 구조의 로컬 데이터베이스

```

---

## 설치 및 실행 방법


### 1. Repository 복제 및 폴더 이동

```bash
# 저장소 클론
git clone [https://github.com/100-hours-a-week/KTB-Sevan-AI.git](https://github.com/100-hours-a-week/KTB-Sevan-AI.git)

# 1주차 프로젝트 폴더로 이동
cd KTB-Sevan-AI/weekChallenge/week_01

### 2. 가상환경 생성 및 활성화

```bash
# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화 (Mac/Linux)
source venv/bin/activate

# 가상환경 활성화 (Windows CMD)
# venv\Scripts\activate.bat

```

### 2. 프로그램 실행 규칙

본 프로그램은 별도의 외부 패키지 설치 없이 파이썬 내장 모듈만으로 구동되므로 즉시 실행이 가능합니다.

```bash
# 링크 추가 실행 구조
python main.py add -u <URL주소> -c <카테고리명>

# 목록 조회 실행 구조
python main.py list (전체 리스트)
python main.py list [-c <카테고리명>]
 
```

---

## 실행 예시

### 1. 새로운 링크 추가 (`add`)

```bash
python main.py add -u "https://docs.python.org/3/" -c "개발_공식문서"

```

*(성공적으로 반영되면 로컬에 `links.json` 파일이 자동 생성되거나 업데이트됩니다.)*

### 2. 전체 목록 조회 (`list` 카테고리 미지정)

```bash
python main.py list

```

**출력 결과:**

```text
전체 목록을 보여드립니다.
========================================
개발_공식문서(1 개)
  - https://docs.python.org/3/
인공지능(2 개)
  - https://chatgpt.com
  - https://gemini.google.com

```

### 3. 특정 카테고리 필터링 조회 (`list -c`)

```bash
python main.py list -c "인공지능"

```

**출력 결과:**

```text
인공지능(2 개)
  - https://chatgpt.com
  - https://gemini.google.com

```

---

## 주제 선정 및 회고

### 회고

* AI를 사용하지 않고 프로그램을 짜려고 노력했다. argparse에 대한 문법을 잘 몰라서 ai의 도움을 받았고 cli의 파일 구조는 어떻게 이루어져야 하는지도 도움을 받았다.
* 그래도 함수를 만든다거나 파일을 불러오고 파일에서 데이터를 출력,저장하는 로직을 스스로 짤 수 있었다.

* - 코딩 할 때 생각해야 할 3가지를 정리하였다.
    - 입력 어떻게 할지 → 입력된 url과 카테고리 문자열을 프로그램으로 어떻게 가져올 것인가
    - 저장은 어떻게 할지 → 로컬 파일에 어떤 형태로 구조화해서 저장할 것인가
    - 출력은 어떻게 보여줄지 → 유저가 보기 좋게 어떤 기호와 줄 바꿈을 사용해 가독성을 높일 것인가

* - 알아야할 문법 툴킷
    1. argparse 와 하위 명령어
        1. subparsers.add_parser(’명령어’) 를 통해 하위 명령어 그룹을 만들고 유저가 args.coomand 에 따라 if else 조건문으로 로직 분기하는 방법
    2. 내장 json 모듈과 파일 입출
        1. json.dump(data, file): 파이썬 딕셔너리를 json형태의 텍스트 파일로 저장
        2. json.load(file): 텍스트 파일을 다시 파이썬 딕셔너리로 읽어올 때 사용
        3. with open(”파일명”, “모드”) as f: 파일을 열고 닫는 과정을 안전하게 처리해줌
    3. 딕셔너리 핸들링
        1. {”개발”: [”url1”, “url2”], “영상”: [”url3”, “url5”]}