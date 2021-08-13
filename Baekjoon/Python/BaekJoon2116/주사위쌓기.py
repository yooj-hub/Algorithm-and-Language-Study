'''
BaekJoon 2116 주사위 쌓기
programmer: yooj
Date: 21.08.13
using: Pycharm  & Python3
Site: https://www.acmicpc.net/problem/2116
'''
import sys

n = int(sys.stdin.readline())  # 주사위의 개수를 입력받음
answer = 0

x = []
dnx = [5, 3, 4, 1, 2, 0]  # 주사위의 마주보는 면을 나타내는 좌표
dc = [0, 1, 2, 1, 2, 0]  # 주사위를 마주보는 면을 기준으로 3개의 케이스로 나눔
for _ in range(n):  # 주사위를 입력 받음
    x.append(list(map(int, sys.stdin.readline().split())))

for i in range(6):  # 6가지 경우가 존재함
    ans = 0
    nx = dnx[i]  # 마주보는 면
    case = dc[i]  # 케이스 설정
    if case == 0:  # 처음에 ans 를 케이스에 따라 제일 큰 값으로 설정
        ans = max(ans, x[0][1], x[0][2], x[0][3], x[0][4])
    elif case == 1:
        ans = max(ans, x[0][0], x[0][2], x[0][4], x[0][5])
    else:
        ans = max(ans, x[0][0], x[0][1], x[0][3], x[0][5])
    for j in range(1, n):
        nx = dnx[x[j].index(x[j - 1][nx])]  # 밑면을 기준으로 잡아서 다음 반댓면을 구함
        case = dc[nx]  # 케이스를 nx 를 기준으로 설정
        mx = 0  # 옆면중 최댓 값을 저장할 변수
        if case == 0:  # 최댓값을 구함
            mx = max(mx, x[j][1], x[j][2], x[j][3], x[j][4])
        elif case == 1:
            mx = max(mx, x[j][0], x[j][2], x[j][4], x[j][5])
        else:
            mx = max(mx, x[j][0], x[j][1], x[j][3], x[j][5])
        ans += mx  # 정답에 더해줌
    if ans > answer:  # 최댓값을 구함
        answer = ans

sys.stdout.write(str(answer))  # 정답 출력
