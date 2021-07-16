# /*
#  * BaekJoon 1068 트리
#  * programmer: yooj
#  * Date: 21.07.17
#  * using: Pycharm & python 3
#  * Site: https://www.acmicpc.net/problem/1068
#  */
#


class Node:  # 문제를 풀기위한 Node 정의

    def __init__(self, uni):  # uni 라는 고유 번호를 가지고 빈 child 리스트를 가지게 생성
        self.uni = uni
        self.child = []

    def setChild(self, a):
        self.child.append(a)


n = int(input())  # 노드의 개수를 입력 받음
data = list(map(int, input().split(" ")))  # 각 부모의 정보를 입력받음
kill = int(input())  # 없앨 노드를 입력 받음
nl = []  # 각 노드를 저장할 노드리스트를 만들음
for i in range(n):  # 각 노드 생성
    nl.append(Node(i))

# 노드에 자식 추가
for i in range(0, n):
    if data[i] == -1:  # 루트 노드일 경우 부모가 없으므로 continue
        continue
    nl[data[i]].setChild(i)  # 루트 노드가 아니면 부모에 자식으로 추가

for i in range(n):
    if kill in nl[i].child:  # kill 을 child 로 가질 경우 제거
        nl[i].child.remove(kill)

cnt = 0
visited = [False] * n  # visited 를 통해 노드가 제거 되었는지 확인


def removeChild(start):  # 없어진 노드의 자식을 모두 없앰
    visited[start] = True  # 지워진 노드의 인덱스를 True
    if len(nl[start].child) == 0:  # child ==0 일 경우 스탑
        return
    for x in nl[start].child:  # 자식들에 대해 제거하는 반복문을 수행
        removeChild(x)


removeChild(kill)  # 함수 작동

for i in range(n):
    if len(nl[i].child) != 0 or visited[i]:  # 리프 노드개수를 구함
        continue
    cnt += 1
print(cnt)  # 정답 출력력
