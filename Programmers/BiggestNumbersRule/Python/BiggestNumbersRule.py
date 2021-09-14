'''
 * Programmers BiggestNumbersRule
 * programmer: yooj
 * using : pycharm & python 3.88
 * Date: 21.06.14
'''

'''
#first Idea
n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)
ans = 0
j = 0
while j != m:
    for i in range(k):
        ans += data[0]
        j += 1
        if (j == m):
            break
        break
    if (j != m):
        ans += data[1]
        j += 1
    else:
        continue

print(ans)
'''
'''
#second Idea
n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))
data.sort(reverse=True)
first = data[0]
second= data[1]
p = data[0]*k + data[1]
ans = p*(m//(k+1))+data[1]*(m%(k+1))
print(ans)
'''
# Third idea
n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))
data.sort()
first = data[-1]
second = data[-2]
count = (m // (k + 1)) * k
count += m % (k + 1)
result = count * first
result += (m - count) * second
print(result)
