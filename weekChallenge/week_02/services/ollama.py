# http 요청 라이브러리 가져오기(비동기)
import httpx

# 함수로 만들어줘야 다른 파일에서 사용할 수 있다.
def request_ollama(content_text: str) -> str:
    # ollama 기본 주소를 상수로 선언
    url = "http://localhost:11434/v1/chat/completions"

    # 내가 보내는 데이터는 json 형태임을 알려주는 방법
    headers = {"Content-Type": "application/json"}

    # 내가 보낼 질문 내용

    payload = {
        "model": "gemma4:e2b",
        "messages" : [
            {"role": "system", "content": " 너는 게시글 내용을 3줄로 요약해주는 AI 어시스턴트입니다."},
            {"role": "user", "content": content_text}
        ],
    }
    # 질문 보내고 기다리기
    response = httpx.post(url, json=payload , headers=headers, timeout = 60.0)

    # 결과 파싱해서 출력하기
    result = response.json()

    return result["choices"][0]["message"]["content"]


