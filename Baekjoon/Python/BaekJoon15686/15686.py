'''
 * Programmers 치킨 배달
 * programmer: yooj
 * using : pycharm & python 3.9.5
 * Date: 21.06.23
 * Site: https://www.acmicpc.net/problem/15686
'''

from itertools import combinations

n, m = map(int, input().split())
city = []
chickenhouse = []
for i in range(n):#도시 입력받기
    city.append(list(map(int, input().split())))
#치킨집이 있는 곳을 chickenhouse 배열에 추가
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chickenhouse.append([i, j])
#combinations를 이용하여 치킨집에 관한 쌍을 전부 찾음
co = list(combinations(chickenhouse, m))


#치킨거리 체크
#s는 m개의 치킨하우스 쌍
def discheck(x, y, s):
    small = 2 * n
    for i in range(len(s)):
        small = min(small, abs(s[i][0] - x) + (abs(s[i][1] - y)))
    return small


cdistance = int(1e9)
#모든 경우의 거리를 구해서 제일 짧은 거리 추출
for k in range(len(co)):#모든 순서쌍에 대하여 계산
    temp = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                temp += discheck(i, j, co[k])
    cdistance = min(cdistance, temp)

print(cdistance)
