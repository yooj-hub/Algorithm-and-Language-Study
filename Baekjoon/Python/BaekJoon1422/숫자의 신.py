# /*
#  * BaekJoon 1422 숫자의 신
#  * programmer: yooj
#  * Date: 21.07.14
#  * using: Pycharm & python 3
#  * Site: https://www.acmicpc.net/problem/1422
#  */
#


import sys

k, n = map(int, sys.stdin.readline().split())  # k 와 n 을 입력받음
data = []
for i in range(k):
    data.append(sys.stdin.readline().rstrip())  # 스트링으로 입력 받음
data.sort(key=lambda x: int(x))  # 스트링의 정렬은 사전순 이므로 제일 큰 수샂가 마지막에 오도록 정렬
for i in range(n - k):  # 제일 큰 수를 추가함
    data.append(data[-1])


def compare(arr, idx1, idx2):  # 두 숫자의 문자열 합이 정상 순서가 클 경우 넘어가고, 아니면 바꿈
    if int(arr[idx1] + arr[idx2]) > int(arr[idx2] + arr[idx1]):
        return
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return


for i in range(n - 1, 0, -1):  # 버블 정렬
    for j in range(i):
        compare(data, i, j)

print("".join(data[::-1]))  # 정답 출력
