'''
BaekJoon 1062 가르침
programmer: yooj
Date: 21.08.07
using: Pycharm  & Python3
Site: https://www.acmicpc.net/problem/1062
'''

import sys

n, k = map(int, sys.stdin.readline().split())  # n 과 k 를 입력 받음
ans = 0
x = [0] * n


def solution(n, k):
    global ans  # 정답을 저장할 전역변수
    strings = []  # 단어를 저장할 strings
    for i in range(n):
        strings.append(sys.stdin.readline().rstrip())
    k -= 5
    for i in range(n):
        for j in range(4, len(strings[i]) - 4):
            # a n t i c 는 무조건 포함되므로 넘김
            if strings[i][j] == 'a' or strings[i][j] == 'n':
                continue
            if strings[i][j] == 't' or strings[i][j] == 'i' or strings[i][j] == 'c':
                continue
            '''
            target 에 a n t i c 를 제외한 알파벳이 있으면 continue 없으면 집합 x[i] 에 추가
            알파벳 차집합 x[i] 집합이 공집합일 경우 다음으로(중복된 알파벳은 더하지 않음)
            '''
            target = 1 << (ord(strings[i][j]) - 97)
            if target & (~x[i]) == 0:
                continue
            x[i] += target

    '''
            조합을 구하는 combination
    '''
    def combination(idx, selected, val):
        if selected == k:  # a n t i c 를 제외한 알파벳을 k 개 선택했을 때 이 집합을 val 에 저장
            global ans
            z = 0
            for i in range(n):
                # x[i] 차집합 val 이 공집합 이면
                if x[i] & (~val) == 0:
                    z += 1
            if ans < z:
                ans = z
            return
        if idx >= 26:
            return
        # 조합 연산
        if idx == ord('a') - 97 or idx == ord('n') - 97 or idx == ord('t') - 97:
            combination(idx + 1, selected, val)
        elif idx == ord('i') - 97 or idx == ord('c') - 97:
            combination(idx + 1, selected, val)
        else:
            combination(idx + 1, selected, val)
            combination(idx + 1, selected + 1, val + (1 << idx))

    # k < 0 일경우 무조건 0개
    if k < 0:
        sys.stdout.write("0\n")
    # 21 일 경우 모든 단어 개수 출력
    elif k == 21:
        sys.stdout.write(str(n) + '\n')
    # 아닐경우 b 부터 콤비네이션 시작
    else:
        combination(1, 0, 0)
        sys.stdout.write(str(ans) + '\n')


if __name__ == '__main__':
    solution(n, k)
