'''
BaekJoon 1078 뒤집음
programmer: yooj
Date: 21.08.02
using: Pycharm  & Python3
Site: https://www.acmicpc.net/problem/1078
'''

import sys
from itertools import product


def solution():
    ans = []
    flag = False  # 정답을 찾았는지 확인하기 위한 변수
    target = int(sys.stdin.readline())  # 목표 값을 입력 받음
    choice = [0]  # 앞에서 1+l 번째 수가 될 경우 양수이고, 중앙을 기준으로 대응되는 수가 될 경우 음수로 설정하였다.
    choice.extend(list(range(-9, 0)))
    choice.extend(list(range(1, 10)))
    f = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]  # 맨 앞이 될 수 있는수 0의 경우 처음을 1, 끝을 1로 두는 경우로 설정하였다.
    if target % 9 != 0:  # 9로 나누어지지 않으면 답이 아니다.
        sys.stdout.write("-1")
        return

    if target == 900000:  # 12 자리의 경우 답이 유일하다.
        sys.stdout.write("100001000001")
        return
    if target == 990000:  # 11 자리의 경우 답이 유일하다.
        sys.stdout.write("10001000001")
        return

    for i in range(0, 5):  # even 은 i * 2 + 2 자리수를 검사 odd 는 i * 2 + 3 자리수를 검사
        s = list(product(choice, repeat=i))  # 중복 순열을 이용하여 대상이 되는 쌍을 구함
        if not flag:  # 같은 자릿수의 수 보다 클 수 없음
            for k in f:  # k 의 값을 선택
                for x in s:  # s 중 1개를 선택하여 사용
                    odd = 0
                    even = 0
                    # 각 자릿수를 만들어 d 와 같은지 조사
                    for j in range(i + 1):
                        if j == 0:
                            even += k * (10 ** (2 * i + 1 - j) - 10 ** j)
                            odd += k * (10 ** (2 * i + 2 - j) - 10 ** j)
                        else:
                            even += x[j - 1] * (10 ** (2 * i + 1 - j) - 10 ** j)
                            odd += x[j - 1] * (10 ** (2 * i + 2 - j) - 10 ** j)
                    # 짝수 자릿수 일 경우
                    if even == target:
                        flag = True
                        n = 0
                        for j in range(i + 1):
                            if j == 0:
                                if k != 0:
                                    n += k * (10 ** (2 * i + 1))
                                else:
                                    n += 1 * (10 ** (2 * i + 1)) + 1
                            else:
                                if x[j - 1] >= 0:
                                    n += x[j - 1] * (10 ** (2 * i + 1 - j))
                                else:
                                    n += x[j - 1] * 10 ** j * (-1)
                        ans.append(n)
                    # 홀수 자릿수 일 경우
                    elif odd == target:
                        flag = True
                        n = 0
                        for j in range(i + 1):
                            if j == 0:
                                if k != 0:
                                    n += k * (10 ** (2 * i + 2 - j))
                                else:
                                    n += 1 * (10 ** (2 * i + 2 - j)) + 1
                            else:
                                if x[j - 1] >= 0:
                                    n += x[j - 1] * (10 ** (2 * i + 2 - j))
                                else:
                                    n += x[j - 1] * (10 ** j) * (-1)
                        ans.append(n)
    # 못찾았으면 -1
    if not flag:
        sys.stdout.write("-1")
    # 찾았으면 정답 출력
    else:
        sys.stdout.write(str(min(ans)))
    return


solution()
