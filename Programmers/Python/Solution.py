'''
 * Programmers Stock Price
 * programmer: yooj
 * using : pycharm & python 3.88
 * Date: 21.06.14
 * Site: https://programmers.co.kr/learn/courses/30/lessons/42584
'''

from collections import deque

def solution(prices):
    answer= deque()
    k=0;
    for i in range (0,len(prices)-1):
        for j in range(i,len(prices)-1):
            print(prices[j])
            if prices[i]<=prices[j]:
                k+=1
            else:
                break
        answer.append(k)
        k=0
    answer.append(0)
    return list(answer)

prices=[1,2,3,2,3]
print(solution(prices))
