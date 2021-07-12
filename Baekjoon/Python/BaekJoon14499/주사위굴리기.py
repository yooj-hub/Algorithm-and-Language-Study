# /*
#  * BaekJoon 주사위 굴리기
#  * programmer: yooj
#  * Date: 21.07.12
#  * using: Pycharm & python3
#  * Site: https://www.acmicpc.net/problem/14499
#  */

from collections import deque

dice = [0, 0, 0, 0, 0, 0]
n, m, x, y, k = map(int, input().split(" "))
data = [[0] * m for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split(" ")))
    for j in range(m):
        data[i][j] = tmp[j]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
tmp = list(map(int, input().split(" ")))
q = deque()  # 덱에 대입
for i in tmp:
    q.append(i)


def checkZero(firstIndex, secondIndex):  # 바닥이 0인지 확인하는 함수
    if data[firstIndex][secondIndex] == 0:
        return True
    return False


def turn(dir):  # 주사위를 회전하는 함수
    global dice
    if dir == 1:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]

    elif dir == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]

    elif dir == 3:  # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

    elif dir == 4:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]


ans = []
while q:  # 입력된 모든 값을 통해 연산
    dir = q.popleft()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 밖을 가마녀
        continue  # 연산에서 제외

    x, y = nx, ny  # 밖을 나가지 않았으므려 x, y에 값 대입
    turn(dir)
    if checkZero(x, y):  # 땅이 0이면
        data[x][y] = dice[5]  # 주사위가 위치하는 면에 밑면의 값을 복사

    elif not checkZero(x, y):  # 땅이 0이 아니면
        dice[5] = data[x][y]  # 주사위의 밑면에 주사위가 위치하는 면의 값을 복사하고,
        data[x][y] = 0  # 주사위가 위치하는 면의 값을 0으로 변경

    ans.append(dice[0])  # 연산에서 얻은 윗면의 값을 추가

for an in ans:
    print(an)
