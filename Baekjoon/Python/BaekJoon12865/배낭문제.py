# /*
#  * BaekJoon 12865 평범한 배낭
#  * programmer: yooj
#  * Date: 21.07.14
#  * using: Pycharm & python 3
#  * Site: https://www.acmicpc.net/problem/12865
#  */
#


n, k = map(int, input().split())  # n , k 를 입력받음
d = [[0] * (k + 1) for _ in range(n)]  # d를 d=[n][k+1]로 초기화
data = []
for i in range(n):
    data.append(list(map(int, input().split(" "))))  # 가방의 목록을 얻음
'''
d[a][b]는 a번 까지 가방의 목록을 조사하였고, b 무게까지의 최댓값을 말한다.
따라서 꺼낸 무게가 b보다 크다면 이전값을 현재값에 업데이트 해준다. 
만약 반대의 경우는 이전 까지 조사한 값중 무게가 b-현재 무게 인 값에 현재 무게를 더한값과 
이전까지 조사한 현재 무게의 값읇 비교하여 더 큰 값을 넣어준다. 

'''

for i in range(n):
    for x in range(1, k + 1):
        a = data[i][0]  # 무게를 입력 받음
        b = data[i][1]  # 가치를 입력 받음
        if x < a:  # 조사해야할 무게가 a 보다 작은 경우 이전 값을 넣어줌
            d[i][x] = d[i - 1][x]
        else:  # 조사해야할 무게 이상인 경우 최대값을 구해줌
            d[i][x] = max(b + d[i - 1][x - a], d[i - 1][x])

print(d[n - 1][k])
