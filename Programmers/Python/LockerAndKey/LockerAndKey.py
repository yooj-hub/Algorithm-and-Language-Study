import copy


def solution(key, lock):
    m = len(key)
    n = len(lock)
    turntime = 0
    count=0
    if count==n:
        return True
    while turntime != 4:
        for i in range(-m+1,n):
            for j in range(-m+1,n):
                temp = copy.deepcopy(lock)
                for k in range(m):
                    for x in range(m):
                        if 0<=i + k < n and 0<=j + x < n:
                            temp[i + k][j + x] += key[k][x]
                if(check(temp)):
                    return True
        key=turn(key)
        turntime += 1
    return False

def check(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if(arr[i][j]!=1):
                return False
    return True

def turn(arr):
    n = len(arr)
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[n - 1 - j][i] = arr[i][j]
    return tmp


key = [[0, 0],[0,0]]
lock = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print(solution(key,lock))

