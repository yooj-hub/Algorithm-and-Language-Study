# /*
#  * BaekJoon 1012 유기농 배추
#  * programmer: yooj
#  * Date: 21.07.13
#  * using: Pycharm & python3
#  * Site: https://www.acmicpc.net/problem/1012
#  */
#


from collections import deque

t = int(input())  # 테스트케이스를 입력받음

# 움직일 수 있는 방향에 대한 설계
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(t):  # 테스트케이스 수 만큼 동작
    ans = 0  # 처음 정답을 0으로 설정
    m, n, k = map(int, input().split(" "))  # n,m,k 를 입력받음
    data = [[0] * m for _ in range(n)]  # m x n 의 data 를 0으로 최기화
    for _ in range(k):  # k 번 입력받음
        a, b = map(int, input().split(" "))  # a,b 에 해당하는 위치에 배추가 있음
        data[b][a] = 1

    # 모든 위치에 대해서 탐색
    for i in range(m):
        for j in range(n):
            if data[j][i] == 1:  # j,i 위치에 배추가 있으면
                ans += 1  # 배추가 있을 때 마다 BFS 를 이용하여 값을 처리함
                # BFS 를 이용한 탐색
                z = deque()
                z.append((j, i))
                data[j][i] = 0
                while z:
                    x, y = z.popleft()
                    for s in range(4):
                        nx = x + dx[s]
                        ny = y + dy[s]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if data[nx][ny] == 1:
                            z.append((nx, ny))
                            data[nx][ny] = 0  # 배추가 있는 곳의 값을 0으로 바꿈
    print(ans)
