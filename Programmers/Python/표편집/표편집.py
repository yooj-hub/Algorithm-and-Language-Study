"""
Programmers 표 편집
Programmer: yooj
Date: 2021 08 08
Using: Python 3 & pycharm
Site: https://programmers.co.kr/learn/courses/30/lessons/81303
"""

from heapq import heappop
from heapq import heappush


def solution(n: int, k: int, cmd: [str]):
    minHeap = []  # min heap
    maxHeap = []  # max heap
    deleted = []  # 지워진 값을 저장할 배열 ( stack 과 같이 동작 )
    for i in range(n):
        heappush(minHeap, i)
    for i in range(k):
        # - 로 넣어 min Heap 으로 구현
        heappush(maxHeap, -heappop(minHeap))
    for x in cmd:
        # 처음에 무슨 명령인지 분류
        com = x[0]
        if com == "D" or com == "U":  # D 와 U 명령은 따로 숫자가 필요하다 2번째 인덱스부터 숫자이므로 그 값을 캐스팅을 통해 얻는다.
            num = int(x[2:])
            # 범위를 벗어나는 경우가 없으므로 따로 다른 처리를 하지 않아도 된다.
            if com == "D":
                for _ in range(num):
                    heappush(maxHeap, -heappop(minHeap))
            else:
                for _ in range(num):
                    heappush(minHeap, -heappop(maxHeap))
        # C 일 경우
        if com == "C":
            deleted.append(heappop(minHeap))
            if len(minHeap) == 0:  # 문제의 조건에 의해 무조건 선택하는 항목이 있어야 하므로 값 1개를 가져온다.
                heappush(minHeap, -heappop(maxHeap))
        # Z 일 경우
        if com == "Z":
            target = deleted.pop()
            cur = minHeap[0]
            # target 보다 클 경우 현재 선택된 값보다 뒤에 있다.
            if target > cur:
                heappush(minHeap, target)
            else:
                heappush(maxHeap, -target)
    check = ["X"] * n
    for i in minHeap:
        check[i] = "O"
    for i in maxHeap:
        check[-i] = "O"
    return ''.join(check)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
