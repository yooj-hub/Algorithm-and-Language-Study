# /*
#  * BaekJoon 6064 카잉달력
#  * programmer: yooj
#  * Date: 21.07.14
#  * using: Pycharm & python 3
#  * Site: https://www.acmicpc.net/problem/6064
#  */
#


t = int(input())  # 테스트 케이스를 입력받음
for _ in range(t):
    m, n, x, y = map(int, input().split(" "))  # m n x y 를 입력 받음
    # x 나 y 가 m , n 인 경우의 예외를 처리함
    if x == m:
        x = 0
    if y == n:
        y = 0
    ans = -1

    # 피벗을 삼기 위한 과정
    if m > n:

        interval = m  # m 이 클경우 m 을 공차로 선정
        divider = n  # n 으로 나누기 연산을 함
        check = y  # 답인지 확인하기 위한 나머지
        if x != 0:  # x 가 m 인 경우 0 부터 시작하는 것을 방지함
            sel = x
        else:
            sel = m
    else:  # 위의 경우의 반대

        interval = n
        divider = m
        check = x
        if y != 0:
            sel = y
        else:
            sel = n

    while sel <= m*n:  # m * n 은 최소 공배수의 배수이므로 모든 경우를 조사 가능
        if sel % divider == check:
            ans = sel
            break
        sel += interval
    print(ans)  # 정답 출력
