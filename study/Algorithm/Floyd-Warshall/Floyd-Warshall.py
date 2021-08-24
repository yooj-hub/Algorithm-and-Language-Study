INF = int(1e9)
VERTEX = 100
vertexes = int(input())
edgees = int(input())

d = [[INF] * VERTEX for _ in range(VERTEX)]

for i in range(1, vertexes + 2):
    d[i][i] = 0

for i in range(edgees):
    f, t, cost = map(int, input().split())
    d[f][t] = cost

for k in range(1, vertexes + 1):
    for a in range(1, vertexes + 1):
        for b in range(1, vertexes + 1):
            if d[a][b] > d[a][k] + d[k][b]:
                d[a][b] = d[a][k] + d[k][b]

for i in range(1, vertexes + 1):
    for j in range(1, vertexes + 1):
        print(d[i][j], end=' ')
    print()

'''

input
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

output
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0 

'''