# /*
#  * Baekjoon3190 Snake
#  * programmer: yooj
#  * Date: 21.06.22
#  * using: IntelliJ & jdk.16.0.1
#  * Site: https://www.acmicpc.net/problem/3190
#  */

def solution():
    n = int(input())#뱀이 지나다닐 공간을 받음
    k = int(input())#사과의 개수
    apple = [[False] * (n + 1) for _ in range(n + 1)]
    directions = [0] * (10001)#시간을 저장하는공간
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(k):#사과 위치 설정
        a, b = map(int, input().split())
        apple[b][a] = True
    s = int(input())
    for i in range(s):#시간에 따른 방향설정
        c, d = map(str, input().split())
        e = 0
        #시간 설정을 1과 -1로하여 dx[dir],dy[dir]로 하여 손 쉽게 사용
        if d == "D":#오른쪽일 경우 1
            e = 1
        else:#왼쪽일 경우 -1
            e = -1
        directions[int(c)] = e
    x = [1]#초기위치 1,1
    y = [1]
    length = 1#초기 길이
    time = 0
    dir = 0#초기 방향(오른쪽)
    while True:
        time += 1#시간 증가
        nx = x[0] + dx[dir]
        ny = y[0] + dy[dir]
        if (0 >= nx or nx > n) or (0 >= ny or ny > n):#벽에 부리치는가(
            return time
        else:#벽에 안부리칠 경우
            x[0], y[0] = nx, ny
            if check(x, y, length) == False:#자기 자신을 먹은 경우 이 떄 몸이 아닌쪽은 지나온 경로이므로 사과가 없음
                return time

            if apple[x[0]][y[0]]:#사과가 있으면
                apple[x[0]][y[0]]=False
                length += 1
                x.append(int(0))#길이 1추가
                y.append(int(0))
                if length == 2:#길이가 처음 증가했을 때
                    x[length - 1] = x[length - 2] - dx[dir]#꼬리 위치 설정
                    y[length - 1] = y[length - 2] - dy[dir]
                    for i in range(length - 2, 0, -1):#나머지 위치 설정
                        x[i] = x[i - 1]
                        y[i] = y[i - 1]
                else:#길이가 3이상일 떄
                    for i in range(length - 1, 1, -1):
                        x[i] = x[i - 1]
                        y[i] = y[i - 1]
                    x[1] = x[0] - dx[dir]#위에서 머리위치를 설정하여 머리기반으로 다시 설정
                    y[1] = y[0] - dy[dir]

            else:#사과를 먹지 않았을 때
                if length >= 2:
                    #꼬리 위치 설정
                    for i in range(length - 1, 1, -1):
                        x[i] = x[i - 1]
                        y[i] = y[i - 1]
                    x[1] = x[0] - dx[dir]#1번째 몸통 위치 설정
                    y[1] = y[0] - dy[dir]
            dir += directions[time]#0이면 방향전환 x 1이면 오른쪽 -1이면 왼쪽
            #exception handling
            if dir == -1:
                dir = 3
            elif dir==4:
                dir=0

#자기 몸을 먹는지 확인
def check(x, y, leng):
    if leng <= 3:
        return True
    else:
        for i in range(2, leng):
            if x[0] == x[i] and y[0] == y[i]:
                return False
        else:
            return True


print(solution())
