"""
/*
 * Programmers 등굣길
 * programmer: yooj
 * Date: 21.07.01
 * using: pycharm & python3
 * Site: https://programmers.co.kr/learn/courses/30/lessons/12900?language=python3
 */
 """

m = 1000000007#모듈러 연산을 위한 m


def solution(n):
    d = [0] * (n + 1)
    global m
    d[0] = 1
    d[1] = 1
    for i in range(2, n + 1):
        d[i] = d[i - 1] % m + d[i - 2] % m#모듈러 법칙 적용
    return d[n] % m


print(solution(4))
