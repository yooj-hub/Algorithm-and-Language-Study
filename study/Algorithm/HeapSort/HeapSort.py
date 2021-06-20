import heapq
#내림차순 heap Sort
h=[]
data=list(map(int,input().split()))
for i in data:
    heapq.heappush(h,-i)
ans=[]
while h:
    ans.append(-heapq.heappop(h))
print(ans)

'''
오름차순 heap Sort
import heapq
h=[]
data=list(map(int,input().split()))
for i in data:
    heapq.heappush(h,i)
ans=[]
while h:
    ans.append(heapq.heappop(h))
print(ans)
'''