# /*
# * 백준 골드바흐의 추측
#  * programmer: yooj
#  * Date: 21.07.07
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/6588
#  */


import sys


def isPrime(n):  # 소수 판별을 위한 ifPrime 함수 정의
    k = 1
    count = 0
    while k * k <= n:  # 에라토스테네스의 체를 이용한 소수판별
        if n % k == 0:
            count += 1
        k += 1
    if count == 1:
        return True
    return False


while True:  # 0이 나올 떄 까지 반복
    n = int(sys.stdin.readline())
    if n == 0:  # 0이 나오면 정지
        break
    a = 3  # 두 홀수의 합이므로 홀수 중 제일 작은 소수는 3임
    b = n - 3  # n-3이 될 수 있는 제일 큰 홀 수이다.
    while True:  # 골드바흐의 추측이 맞는지 확인
        if not isPrime(a) or not isPrime(b) and a < b:  # 둘중 하나라도 소수가 아니고 a가 b보다 작은 겨웅
            a += 2
            b -= 2
            continue
        if isPrime(a) and isPrime(b):  # 둘다 홀 수 인 경우 a가 최소값에서 시작하여 문제에 해당하는 값이 제일 먼저 출력되고 정지됨
            print("%d = %d + %d" % (n, a, b))
            break
        if a > b:  # a가 b보다 클 경우 골드바흐의 추측이 틀린게 됨
            print("Goldbach's conjecture iw wrong.")
            break
