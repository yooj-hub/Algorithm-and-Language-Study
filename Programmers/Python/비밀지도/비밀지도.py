from collections import deque


def solution(n: int, arr1: [int], arr2: [int]):
    ans = [[" "] * n for _ in range(n)]
    change(ans, arr1, n)
    change(ans, arr2, n)
    answer=[]
    for i in range(n):
        answer.append(''.join(ans[i]))
    return answer


def change(answer, arr, n):
    for i in range(n):
        t = getBin(arr[i], n)
        for j in range(n):
            if t[j] == '#':
                answer[i][j] = t[j]


def getBin(a: int, n: int):
    b = deque()
    while a:
        if a % 2:
            b.append("#")
        else:
            b.append(" ")
        a //= 2
    b.reverse()
    while len(b) != n:
        b.appendleft(" ")
    b = list(b)
    return b


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
