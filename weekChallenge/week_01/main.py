'''
    링크 관리 프로그램

    1. 링크와 카테고리 입력받기
    2. 링크 저장하기 (url, category)
    3. 완료 되었다고 출력하기

'''

import argparse
import manager

def main():
    parser = argparse.ArgumentParser(description="linkcat: url 분류기")
    subparsers = parser.add_subparsers(dest ="command", required = True)

    # add 명령어 설정
    add_parser = subparsers.add_parser("add", help = "새로운 링크 추가")
    add_parser.add_argument("-u", "--url", required=True, help ="저장할 url")
    add_parser.add_argument("-c", "--category", required=True, help ="분류할 카테고리")

    # list 명령어 설정
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("-c", "--category")

    args = parser.parse_args()

    if args.command =="add":
        # url 과 카테고리를 저장
        manager.save_link(args.url, args.category)
    elif args.command =="list":
        # 저장된 리스트를 출력
        manager.list_link(args.category)

if __name__ == "__main__":
    main()