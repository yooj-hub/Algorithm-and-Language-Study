# /*
#  * BaekJoon 1248 맞춰봐
#  * programmer: yooj
#  * Date: 21.07.20
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/1248
#  */

import sys

n = int(sys.stdin.readline())  # 수열의 크기를 알려줌
txt = sys.stdin.readline().rstrip()  # -+0 으로 이루어진 문자열을 입력받음
data = [[''] * n for _ in range(n)]
pp = 0
first = []
for i in range(n):  # 정답에 맞추어 data 에 배치함
    for j in range(i, n):
        data[i][j] = txt[pp]
        pp += 1
        if i == j:
            first.append(txt[pp - 1])


def dfs(idx, numbers):  # 답을 구하는 함수
    global n
    if idx == n:
        makeS(idx + 1, numbers)
        return
    if first[idx] == '+':
        for i in range(1, 11):
            numbers.append(i)
            if makeS(idx + 1, numbers):  # 백 트랙킹 방식을 차용하여 미리 검사함
                dfs(idx + 1, numbers)
            numbers.pop()
    elif first[idx] == '0':  # 항상 옳음
        numbers.append(0)
        dfs(idx + 1, numbers)
        numbers.pop()
    else:
        for i in range(1, 11):
            numbers.append(-i)
            if makeS(idx + 1, numbers):  # 백 트랙킹 방식을 차용하여 미리 검사함
                dfs(idx + 1, numbers)
            numbers.pop()


def makeS(idx, numbers):
    global n
    if idx == n + 1:  # 전부다 검사 한 경우 이므로 출력
        sys.stdout.write(' '.join(map(str, numbers)))
        sys.exit(0)
    else:
        for j in range(idx):
            key = sum(numbers[j:idx + 1])  # 합계를 구함
            # 맞는지 확인
            if key > 0 and data[j][idx - 1] == '+':
                continue
            elif key < 0 and data[j][idx - 1] == '-':
                continue
            elif key == 0 and data[j][idx - 1] == '0':
                continue
            else:
                return False
        return True


dfs(0, [])
