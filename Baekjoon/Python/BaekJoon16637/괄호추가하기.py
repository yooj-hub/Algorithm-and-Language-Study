'''
BaekJoon 16637 괄호 추가하기
programmer: yooj
Date: 21.08.11
using: Pycharm  & Python3
Site: https://www.acmicpc.net/problem/16637
'''

import copy
import sys

n = int(sys.stdin.readline())
exp = sys.stdin.readline().rstrip()
numbers = []  # 숫자를 저장하는 배열
oper = []  # 연산자를 저장하는 배열
for i in range(len(exp)):
    if i % 2 == 0:
        numbers.append(int(exp[i]))
    else:
        oper.append(exp[i])
ans = -int(3e9)  # -2^31 은 -21억 이므로 넉넉하게 -30억으로 지정
l = len(oper)  # 연산자의 개수 저장

for i in range((1 << l)):  # 0 ~ l-1 까지의 비트연산 합은 2^l -1 이므로 다음과 같이 작성
    orders = []
    flag = True
    for k in range(l):  # 해당하는 케이스에 우선되는 연산자에 대한 선택을 시행함

        if (i & (1 << k)) != 0:  # 우선되는 연산순서에 포함 될 경우
            orders.append(k)
            if k != 0:
                if (i & (1 << k - 1)) != 0:
                    flag = False  # 연속 되는 경우
                    break
    if flag:  # 연속되지 않을 때
        oper2 = oper
        numbers2 = numbers
        p = 0
        for x in orders:  # 우선 되는 연산에 대한 연산
            x -= p
            p += 1
            if oper2[x] == '+':
                t = numbers2[x] + numbers2[x + 1]
            elif oper2[x] == '*':
                t = numbers2[x] * numbers2[x + 1]
            else:
                t = numbers2[x] - numbers2[x + 1]
            oper2 = oper2[:x] + oper2[x + 1:]
            numbers2 = numbers2[:x] + [t] + numbers2[x + 2:]
        while len(oper2) != 0:  # 나머지를 연산
            if oper2[0] == '+':
                t = numbers2[0] + numbers2[0 + 1]
            elif oper2[0] == '*':
                t = numbers2[0] * numbers2[0 + 1]
            else:
                t = numbers2[0] - numbers2[0 + 1]
            oper2 = oper2[:0] + oper2[0 + 1:]
            numbers2 = numbers2[:0] + [t] + numbers2[0 + 2:]
        if ans < numbers2[0]:  # 최댓값을 구함
            ans = numbers2[0]

sys.stdout.write(str(ans))
