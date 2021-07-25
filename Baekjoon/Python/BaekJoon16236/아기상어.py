# /*
#  * BaekJoon 16236 아기상어
#  * programmer: yooj
#  * Date: 21.07.25
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/16236
#  */

import sys
from collections import deque

n = int(sys.stdin.readline())  # 맵의 크기를 입력을 받음
data = []
fish = [0] * 7
a, b = 0, 0
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))  # data 에 입력을 저장
for i in range(n):
    for j in range(n):
        if 0 < data[i][j] < 7:  # 1 ~ 6은 물고기 이므로 물고기의 마릿수를 저장함
            fish[data[i][j]] += 1  # 마릿수 저장
        elif data[i][j] == 9:  # 9 는 상어의 위치
            data[i][j] = 0  # 상어의 위치를 빈 공간으로 만듦
            a, b = i, j  # a b 는 상어의 위치를 나타냄


def eatable():  # 먹을 것이 있는지 판단하는 함수
    for i in range(1, s):
        if fish[i] > 0:
            return True
    return False


# 갈 수 있는 방향
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
food = 0  # 먹은 마릿수
s = 2  # 처음 크기
ans = 0
t1, t2, t3 = a, b, 0


def sizeUp():  # 상어를 성장시키는 함수
    global food
    global s
    if s <= 6:
        if food == s:
            s += 1
            food = 0


q = deque()  # bfs 를 위한 덱 선언
l = [(a, b, 0)]
while eatable():  # 먹을 것이 있을경우
    if len(l) >= 1:  # 먹을 곳에 가는 경로가 있는 경우
        l.sort(key=lambda x: (x[2], x[0], x[1]))  # 가는데 걸린 시간, x , y 순으로 정렬
        ans = l[0][2]  # 답이 될 수 잇는 시간을 저장
        q.append(l[0])  # q 에 시작으로 조건에 맞는 값을 저장
        fish[data[l[0][0]][l[0][1]]] -= 1  # fish 배열에서 해당하는 크기의 물고기 마릿수 1을 낮춤
        data[l[0][0]][l[0][1]] = 0  # 빈칸으로 만들음
        l.clear()  # l 배열을 비움
        visited = [[False] * n for _ in range(n)]  # visited 배열을 False 로 초기화
        visited[q[0][0]][q[0][1]] = True  # 시작 위치를 들린것으로 처리
        flag = True  # 먹었을 경우 탐색을 멈추기 위한 변수
    else:  # l 배열의 크기가 0 이면 먹은 것이 없으므로 종료
        break
    while q:
        x, y, t = q.popleft()  # x y 는 위치 t 는 시간
        for i in range(4):  # 갈 수 있는 방향 모두 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:  # 인덱스를 벗어날 경우 continue
                continue
            if not visited[nx][ny] and 0 < data[nx][ny] < s:  # 간 적이 없고 먹을 수 있는 경우
                visited[nx][ny] = True  # 간 것으로 처리
                l.append((nx, ny, t + 1))  # l 배열에 위치와 시간을 저장
                flag = False  # 먹었으면 false 로 바꿔서 탐색을 멈춤
                continue
            if not visited[nx][ny] and data[nx][ny] <= s and flag:  # 간 적이 없고 통과할 수 있는 경우
                visited[nx][ny] = True  # 간 것으로 처리
                q.append((nx, ny, t + 1))  # q 에 추가하여 더 탐색함
    food += 1  # 먹었을 경우 +1 만약 안먹었을 경우 위의 l 배열이 0 이므로 종료돼 상관 없음
    sizeUp()  # 크기가 증가하는지 확인하고, 크기가 증가하면 증가시킴

print(ans)  # 정답 출력
