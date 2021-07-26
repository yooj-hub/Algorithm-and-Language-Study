# /*
#  * BaekJoon 2493 탑
#  * programmer: yooj
#  * Date: 21.07.26
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/2493 탑
#  */
import sys

n = int(sys.stdin.readline())  # 탑의 개수를 입력 받음
stk1 = []  # 처음 인덱스와 값을 저장하기 위한 스택
stk2 = []  # 답을 체크하기 위한 스택
ans = [0] * (n + 1)  # 0으로 초기화 함
data = list(map(int, sys.stdin.readline().split()))  # 한 줄을 입력 ㅂ다음
for i in range(n):  # 스택에 입력
    stk1.append((i + 1, data[i]))
while stk1:  # 스택 1이 비지 않았으면
    if len(stk1) == 1:  # stk1 의 길이 1이면 그 탑은 전송할 곳이 없음
        break
    stk2.append((stk1.pop()))  # 스택 2에 스택 1의 최상단을 추가
    while stk2 and stk1[-1][1] > stk2[-1][1]:  # stk2 가 존재하고 다음 탑이 이전 탑들보다 길경우 정답을 입력함
        ans[stk2[-1][0]] = stk1[-1][0]
        stk2.pop()  # 답을 입력한 타워는 제거

sys.stdout.write(' '.join(map(str, ans[1:])))  # 정답 출력
