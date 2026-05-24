# # http 요청 라이브러리 가져오기(비동기)
# import httpx

# # ollama 기본 주소를 상수로 선언
# url = "http://localhost:11434/v1/chat/completions"

# # 내가 보내는 데이터는 json 형태임을 알려주는 방법
# headers = {"Content-Type": "application/json"}

# # 내가 보낼 질문 내용

# payload = {
#     "model": "gemma4:e2b",
#     "messages" : [
#         {"role": "system", "content": " 너는 게시글/댓글 내용을 요약해주는 AI 어시스턴트입니다."},
#         {"role": "user", "content": " 카테부(카카오테크 부트캠프) AI 실무' 과정은 카카오 현직자가 직접 커리큘럼을 설계하고 멘토링을 제공하는 실전형 인공지능 부트캠프입니다. Python, 머신러닝, LLM 기반 서비스 구현 등 현업에 즉시 투입 가능한 실무 기술을 약 6개월간 1,000시간 집중 학습합니다.[주요 교육 내용]프로그래밍 및 웹: 파이썬, FastAPI를 활용한 고성능 웹 API 서버 구축 및 데이터 활용.인공지능 핵심: 머신러닝, 딥러닝, NLP(자연어 처리), Transformer 모델 이해.생성형 AI 및 배포: LLM 기반 서비스 개발, 해커톤 및 멘토링을 통한 실제 서비스 설계 및 배포.[교육 지원 및 혜택]교육 환경: 판교 오프라인 교육장 1인 1석 제공, 고사양 GPU 클라우드 환경 및 유료 AI 도구 지원.커리어 지원: 카카오 현직자의 1:1 코드리뷰 및 이력서/포트폴리오 취업 컨설팅.수업 방식: 온라인과 오프라인(경기도) 혼합 방식으로 진행되며, 고용노동부 내일배움카드 발급 대상자라면 전액 국비 지원으로 참여 가능.더 자세한 커리큘럼 확인 및 기수별 모집 일정은 카카오테크 부트캠프 공식 홈페이지에서 확인하실 수 있습니다."}
#     ],
# }
# # 질문 보내고 기다리기
# response = httpx.post(url, json=payload , headers=headers, timeout = 60.0)

# # 결과 파싱해서 출력하기
# result = response.json()

# print(result["choices"][0]["message"]["content"])


