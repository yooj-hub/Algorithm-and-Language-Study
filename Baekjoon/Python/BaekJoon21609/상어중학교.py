# /*
#  * BaekJoon 상어중학교
#  * programmer: yooj
#  * Date: 21.07.24
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/21609
#  */

import sys

n, m = map(int, sys.stdin.readline().split())  # n 과 m 을 입력받음
graph = []
for i in range(n):  # graph 에 해당하는 값 저장
    graph.append(list(map(int, sys.stdin.readline().split())))

ans = 0
# 움직일 수 잇는 방향
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while True:
    a = []
    score = 0  # 얻는 점수
    rainbow = 0  # 무지개 블록의 개수
    visited = [[False] * n for _ in range(n)]  # 움직임을 기록하기 위한 visited
    zero = []  # 지나간 0을 저장하는 배열


    def dfs(x, y, p, r):  # x , y 는 현재 위치 p 는 현재 수,  r 은 무지개 여부
        global rainbow
        global score
        score += 1  # 호출되면 score +1
        if r == 1:  # 무지개 이면 무지개 +1
            rainbow += 1
        for i in range(4):  # 갈 수 잇는 모든 방향 조사
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:  # 범위 초과시 continue
                continue

            if not visited[nx][ny]:  # 들리지 않았으면
                if graph[nx][ny] == p:  # 무지개 블록이아닌 검정이 아닌 블록일 경우
                    visited[nx][ny] = True  # nx, ny 를 들린것으로 처리
                    dfs(nx, ny, p, 0)  # 재귀 호출
                elif graph[nx][ny] == 0:
                    zero.append((nx, ny))  # 들린 zero list 에 nx ny 추가
                    visited[nx][ny] = True  # 들린 것으로 처리
                    dfs(nx, ny, p, 1)  # 재귀 호출


    def dfsDelete(x, y, p):  # x y 에 대하여 p 색에 대하여 삭제하는 함수
        # 갈 수 잇는 모든 방향 조사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:  # 범위 초과시 continue
                continue
            if graph[nx][ny] == p and visited[nx][ny]:  # 위의 dfs 에서 true 처리 했으므로 true 기반으로 실행
                visited[nx][ny] = False  # 들린 것으로 처리
                graph[nx][ny] = -2  # -2 를 빈 칸으로 설정
                dfsDelete(nx, ny, p)  # 재귀 호출
            elif graph[nx][ny] == 0:  # 0 이면 -2 로 바꾸고 재귀 호출
                graph[nx][ny] = -2
                dfsDelete(nx, ny, p)


    def gravity():  # 중력 적용 함수
        for i in range(n - 2, -1, -1):  # 아래부터 호출함
            for j in range(n):
                if graph[i][j] >= 0:
                    k = i + 1  # 바로 아랫갑승ㄹ k 로 설정
                    while k < n and graph[k][j] == -2:  # 빈칸이면
                        graph[k - 1][j], graph[k][j] = graph[k][j], graph[k - 1][j]  # swap
                        k += 1


    def turnCounterClockCycle():  # 반시계로 회전하는 함수
        data = []
        for i in range(n - 1, -1, -1):
            z = []
            for j in range(n):
                z.append(graph[j][i])
            data.append(z)
        return data


    for i in range(n):  # 제일 행과 열이 작은 것 부터이므로 낮은 수부터 시작
        for j in range(n):
            if graph[i][j] > 0 and not visited[i][j]:
                zero = []
                score = 0
                rainbow = 0
                visited[i][j] = True
                dfs(i, j, graph[i][j], 0)
                a.append((i, j, rainbow, score))
                for t in zero:
                    visited[t[0]][t[1]] = False
    # 스코어, 무지개, 행 , 열 전부 내림차 순으로 정렬
    a.sort(key=lambda x: (-x[3], -x[2], -x[0], -x[1]))
    if a:
        if a[0][3] <= 1:  # 스코어가 1 이하면 종료
            break
        else:
            ans += a[0][3] * a[0][3]  # 점수를 더해줌
            v = graph[a[0][0]][a[0][1]]  # v 값은 지워지는 색
            graph[a[0][0]][a[0][1]] = -2  # 지워지는 곳의 시작점을 없앰
            visited[a[0][0]][a[0][1]] = False  # 들린 것으로 처리
            dfsDelete(a[0][0], a[0][1], v)  # 삭제
            gravity()  # 중력
            graph = turnCounterClockCycle()  # 회전
            gravity()  # 중력
    else:  # a 가 존재하지 않으면 break
        break
sys.stdout.write(str(ans))  # 정답 출력
