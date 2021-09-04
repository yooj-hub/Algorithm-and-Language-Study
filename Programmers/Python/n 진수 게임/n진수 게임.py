"""
Programmers n 진수 게임
Programmer: yooj
Date: 2021 09 04
Using: Python 3 & pycharm
Site:https://programmers.co.kr/learn/courses/30/lessons/17687
"""


def solution(n: int, t: int, m: int, p: int):
    alp = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]  # n 진수에서 대응되는 값을 저장
    pt = 0  # 현재 10진수로 어떤 수를 나타내는지 확인하기 위한 pt
    s = []  # 정답을 저장하는 s
    v = 0  # 현재 저장된 수의 개수를 확인하기위한 v
    p -= 1  # 나머지 연산을 할경우 1순번 일경우 0순번으로 계산해야한다.
    k = 0  # 현재 진행된 순서를 나타내는 k
    while v < t:
        z = pt  # 현재 n 진법으로 바꾸기 위한 수를 나타낸다.
        pt += 1  # 다음 수로 변경
        q = []  # n 진법으로 변경된 수를 저장할 배열

        # n 진법 변경
        while z != 0:
            q.append(alp[z % n])
            z //= n
        q.reverse()
        # len(q) == 0 일 경우 0을 연산한 것이므로 0 을 추가한다.
        if len(q) == 0:
            q.append(0)
        # 순번에 맞는 경우를 s 에 넣어준다.
        for j in range(len(q)):
            if k % m == p:  # 순번이 맞을 경우 s 에 입력
                s.append(q[j])
                v += 1
            k += 1
    # 길이 이상이 될 경우 자른다.
    while len(s) != t:
        s.pop()
    return ''.join(map(str, s))


print(solution(2, 4, 2, 1))
