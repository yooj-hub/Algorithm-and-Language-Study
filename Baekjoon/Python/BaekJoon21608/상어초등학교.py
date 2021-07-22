# /*
#  * BaekJoon 상어초등학교
#  * programmer: yooj
#  * Date: 21.07.22
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/21608
#  */
import sys

n = int(sys.stdin.readline())
data = [[0]]  # 첫 값을 미리 지정해 둠 ( 입력된 사람과 맞추기 위해 더미 추가 )
for _ in range(n * n):  # 입력 받음
    data.append(list(map(int, sys.stdin.readline().split())))

# 좋아하는 학생 조사 방향
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

graph = [[0] * (n + 1) for _ in range(n + 1)]  # 1행과 1열을 더미로 두고 만듦


def selectPos(idx):  # 놓을 위치 선정
    check = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == 0:
                p = 0  # 좋아하는 학생의 수
                e = 0  # 빈 자리
                for x in range(4):
                    nx = i + dx[x]
                    ny = j + dy[x]
                    if nx <= 0 or ny <= 0 or nx > n or ny > n:
                        continue
                    if graph[nx][ny] in data[idx][1:]:  # 좋아하는 학생이면
                        p += 1
                    elif graph[nx][ny] == 0:  # 빈자리면
                        e += 1
                check.append((p, e, i, j))  # 좋아하는학생수, 빈자리, 현재 위치를 넣음

    check.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))  # 좋아하는 학생수 내림차, 빈자리 내림차, 현재위치 오름차로 정렬함
    graph[check[0][2]][check[0][3]] = data[idx][0]  # 가장 앞에 있는 원소를 선택함


def getScore():  # 호감도 계산
    score = 0
    for i in range(1, n + 1):  # 모든 학생의 호감도를 조사함
        for j in range(1, n + 1):
            p = graph[i][j]  # i,j 번 사람을 기준으로 조사
            k = 0
            # 자신이 data 배열의 몇 번째인지 확인
            for u in range(1, n * n + 1):
                if p == data[u][0]:
                    k = u # 자신의 위치를 저장
                    break
            person = 0
            # 호감도 계산
            for x in range(4):
                nx = i + dx[x]
                ny = j + dy[x]
                if nx <= 0 or ny <= 0 or nx > n or ny > n:
                    continue
                if graph[nx][ny] in data[k][1:]: # 0 번 자리는 자기 자신이므로 제외
                    person += 1
            if person == 4:
                score += 1000
            elif person == 3:
                score += 100
            elif person == 2:
                score += 10
            elif person == 1:
                score += 1
    return score


for q in range(1, n * n + 1):
    selectPos(q) # 모든 학생 자리 선택
sys.stdout.write(str(getScore())) # 점수 출력
