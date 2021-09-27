import sys
from collections import deque

t = int(sys.stdin.readline())


def l_calc(num):
    return (num * 10) % 10000 + num // 1000


def r_calc(num):
    return num//10+(num%10)*1000


def d_calc(num):
    return (num * 2) % 10000


def s_calc(num):
    if num == 0:
        return 9999
    else:
        return num - 1


for _ in range(t):
    pre = [""] * 10001
    pren = [-1] * 10001
    visited = [False] * 10001
    start, target = map(int, sys.stdin.readline().split())
    q = deque()
    q.append(start)
    answer = ""
    visited[start] = True
    while q:
        cur = q.popleft()
        if cur == target:
            stk = []
            while cur != -1:
                stk.append(pre[cur])
                cur = pren[cur]
            while stk:
                answer += stk.pop()
            break
        d_cur = d_calc(cur)
        s_cur = s_calc(cur)
        l_cur = l_calc(cur)
        r_cur = r_calc(cur)

        if not visited[d_cur]:
            visited[d_cur] = True
            q.append(d_cur)
            pre[d_cur] = "D"
            pren[d_cur] = cur

        if not visited[s_cur]:
            visited[s_cur] = True
            q.append(s_cur)
            pre[s_cur] = "S"
            pren[s_cur] = cur

        if not visited[l_cur]:
            visited[l_cur] = True
            q.append(l_cur)
            pre[l_cur] = "L"
            pren[l_cur] = cur

        if not visited[r_cur]:
            visited[r_cur] = True
            q.append(r_cur)
            pre[r_cur] = "R"
            pren[r_cur] = cur

    print(answer)
