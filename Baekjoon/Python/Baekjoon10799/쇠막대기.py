# /*
#  * BaekJoon 10799 쇠막대기
#  * programmer: yooj
#  * Date: 21.07.18
#  * using: Pycharm & python 3
#  * Site: https://www.acmicpc.net/problem/10799
#  */
#

import sys

data = list(map(str, sys.stdin.readline().rstrip()))  # 괄호 문자열을 입력 받음
a = []  # 공백리스트 선언
cnt = 0
for i in range(len(data)):
    if data[i] == '(':  # 왼쪽 괄호의 인덱스를 스택에 넣음
        a.append(i)
    if data[i] == ')':  # 오른쪽 괄호일 경우 2가지 상황이 가능함
        if a[-1] == i - 1:  # 바로 전이 왼쪽 괄호인 경우 레이저가 나감
            a.pop()  # 맨 끝 왼쪽 괄호 제거
            cnt += len(a)  # 남은 왼쪽 괄호 만큼이 쇠막대기 이므로 그 만큼 증가함
        else:  # 아닐 경우 괄호가 끝나고 마지막으로 한 조각이 됨
            a.pop()
            cnt += 1
print(cnt)
