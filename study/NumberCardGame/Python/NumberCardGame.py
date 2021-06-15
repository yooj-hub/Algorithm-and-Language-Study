'''
 * Programmers NumberCardGame
 * programmer: yooj
 * using : pycharm & python 3.88
 * Date: 21.06.14
'''

N, M = list(map(int, input().split()))

result= 0
for i in range(N):
    Min=min(list(map(int, input().split())))
    result=max(result,Min)
print(result)