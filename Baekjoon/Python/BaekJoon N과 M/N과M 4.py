# 중복 조합

import sys

n, m = map(int, input().split(" "))
ans = [0] * m


def dfs(idx, selected, n, m):  # idx 의 숫자를 고르는 상황
    if selected == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    if idx > n:
        return
    ans[selected] = idx  # idx 를 선택함
    dfs(idx, selected + 1, n, m)  # idx 를 선택한 후 재귀
    ans[selected] = 0
    dfs(idx + 1, selected, n, m)  # idx 를 선택하지 않음


cnt = [0] * 10


def dfs2(idx, selected, n, m):  # idx 를 선택하는 기준으로 판별
    if selected == m:  # m 개를 선택한 경우
        # 출력
        for i in range(1, n + 1):
            for j in range(1, cnt[i] + 1):
                print(i, end=" ")
        print()
        return
    # 고를 수가 n 보다 큰 경우
    if idx > n:
        return
    for x in range(m - selected, 0, -1):  # m-selected 개 부터 1개 고른 경우까지
        cnt[idx] = x  # idx 를 x 개 고름
        dfs(idx + 1, selected + x, n, m)  # selected 개를 다른 수를 고르고 그 이후 idx 를 x 개 고른 경우를 뜻함
    cnt[idx] = 0
    dfs(idx + 1, selected, n, m)  # idx 의 숫자를 안 고른 경우우


dfs(1, 0, n, m)
