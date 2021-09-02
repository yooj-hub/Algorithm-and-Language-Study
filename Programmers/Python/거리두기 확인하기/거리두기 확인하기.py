"""
Programmers 거리 두기 확인하기
Programmer: yooj
Date: 2021 09 02
Using: Python 3 & pycharm
Site: https://programmers.co.kr/learn/courses/30/lessons/81302
"""

from collections import deque


def solution(places):
    answer = []
    # 움직이는 방향
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for case in places:
        # 거리두기를 확인 하는 변수
        check = True
        # 자기 자신을 다시 찾는 경우를 방지하기 위한 방문 확인 배열
        visited = [[False] * 5 for _ in range(5)]
        for i in range(5):
            if not check:
                break
            else:
                for j in range(5):
                    # 사람이 있을 경우 BFS 를 수행해서 거리안에 사람이 있는지 확인한다.
                    if case[i][j] == "P":
                        q = deque()
                        q.append([i, j, 0])
                        visited[i][j] = True
                        while q:
                            x, y, cnt = q.popleft()
                            for c in range(4):
                                nx = x + dx[c]
                                ny = y + dy[c]
                                # 범위 안만 탐색
                                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                                    continue
                                # 파티션 일 경우 무시
                                if case[nx][ny] == "X":
                                    continue
                                # 자기 자신이 아니고, 사람이 있을 경우 ( 무조건 양방향으로 거리가 2 이므로 이전에 처리한 것은 상관이 없음 )
                                if case[nx][ny] == "P" and not visited[nx][ny]:
                                    check = False
                                    break
                                # 빈 테이블 일 경우 큐에 삽입
                                if case[nx][ny] == "O":
                                    # cnt = 1 일 경우 다음 탐색시 거리가 3이 된다.
                                    if cnt != 1:
                                        q.append([nx, ny, cnt + 1])
                    if not check:
                        break
        # 거리두기를 했으면 1 안했으면 0
        if check:
            answer.append(1)
        else:
            answer.append(0)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
