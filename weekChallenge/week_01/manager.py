import os
import json

def load_db():
    '''
    links.json 파일이 존재하는지 확인
    있으면 딕셔너리로 반환
    없으면 {} 반환
    '''
    if os.path.exists("links.json"):
        with open("links.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data 
    else:
        return {}
    
# url, category를 받아서 작성할 수 있도록 해야한다
def save_link(url,category):
    # 일단 links.json을 db에 담아
    db = load_db()
    if category not in db:
        db[category] = []

    if url not in db[category]:
        db[category].append(url)

    with open("links.json", "w", encoding="utf-8") as f:
        json.dump(db,f,ensure_ascii=False, indent=4)

def list_link(category=None):
    db = load_db()
    if not db:
        print("저장된 링크가 없습니다.")

    if category is None:
        print("전체 목록을 보여드립니다.")
        print("="*40)
        # 파이썬 딕셔너리 뒤에 .items()를 붙이면, 
        # 파이썬은 딕셔너리 안에 있는 데이터를 [이름표(Key)]와 [내용물(Value)] 쌍으로 묶어서 
        # 하나씩 밖으로 던져줍니다.
        for name, url_list in db.items():
            print(f'{name}({len(url_list)} 개)')
            
            for url in url_list:
                print(f"  - {url}")
    else:
        if category in db:
            url_list = db[category]
            print(f'{category}({len(url_list)} 개)')
            for url in url_list:
                print(f"  - {url}")
            print(url_list)
        else:
            print("해당 카테고리가 존재하지 않습니다.")