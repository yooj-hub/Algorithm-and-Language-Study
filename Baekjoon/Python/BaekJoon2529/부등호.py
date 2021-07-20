# /*
#  * BaekJoon 2529 부등호
#  * programmer: yooj
#  * Date: 21.07.20
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/2529
#  */

n = int(input())  # 부등호의 개수를 입력 받음
data = list(map(str, input().split()))  # 부등호를 입력 받음
visited = [False] * 10  # 사용한 수인지 체크하는 배열
first = True  # 처음을 찾았는지 확인하는 변수
last = True  # 마지막을 찾았는지 확인하는 변수


def dfsFirst(idx, n, numbers):  # 제일 작은 만족하는 수를 구하는 함수
    global first
    if idx == n + 1 and first:  # 처음을 찾지 못했고 모든 수를 찾은 경우
        print(''.join(map(str, numbers)))  # 정답 출력
        first = False  # 처음을 찾았으므로 종료
        return
    if idx > n:
        return
    if first:
        if idx == 0:
            for i in range(10):  # 첫 수에 대한 입력
                numbers.append(i)
                visited[i] = True  # i 번 수를 사용한 것을 남김
                dfsFirst(idx + 1, n, numbers)
                visited[i] = False  # 다음 수를 위해 다시  False 로 돌림
                numbers.pop()
        else:  # 그 이외의 수
            for i in range(10):
                if not visited[i] and first:
                    if data[idx - 1] == '<':
                        if numbers[idx - 1] < i:
                            numbers.append(i)
                            visited[i] = True
                            dfsFirst(idx + 1, n, numbers)
                            visited[i] = False
                            numbers.pop()
                    else:
                        if numbers[idx - 1] > i:
                            numbers.append(i)
                            visited[i] = True
                            dfsFirst(idx + 1, n, numbers)
                            visited[i] = False
                            numbers.pop()


def dfsLast(idx, n, numbers):  # 마지막 수에 대해 구하는 함수
    global last
    if idx == n + 1 and last:
        print(''.join(map(str, numbers)))
        last = False
        return
    if idx > n:
        return
    if last:
        if idx == 0:
            for i in range(9, -1, -1):
                numbers.append(i)
                visited[i] = True
                dfsLast(idx + 1, n, numbers)
                visited[i] = False
                numbers.pop()
        else:
            for i in range(9, -1, -1):
                if not visited[i] and last:
                    if data[idx - 1] == '<':
                        if numbers[idx - 1] < i:
                            numbers.append(i)
                            visited[i] = True
                            dfsLast(idx + 1, n, numbers)
                            visited[i] = False
                            numbers.pop()
                    else:
                        if numbers[idx - 1] > i:
                            numbers.append(i)
                            visited[i] = True
                            dfsLast(idx + 1, n, numbers)
                            visited[i] = False
                            numbers.pop()


dfsLast(0, n, [])
dfsFirst(0, n, [])
