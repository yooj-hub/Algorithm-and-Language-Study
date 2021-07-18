def next_permutation(a):  # 바로 다음 순열을 구하는 알고리즘
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
d = list(range(n)) # 0 ~ n-1 까지 입력
ans = int(1e9)  # 충분히 큰 값으로 설정
while True:
    check = True
    s = 0
    for i in range(0, n - 1):
        if w[d[i]][d[i + 1]] == 0: # 0 이면 갈 수 없는 곳이므로 스킵
            check = False
            break
        else:
            s += w[d[i]][d[i + 1]] # 0이 아닌 경우 갈 수 있으므로 더해줌
    if check and w[d[-1]][d[0]] != 0: # 0 으로 가는게 가능하면
        s += w[d[-1]][d[0]] # 더하고 정답 계산
        ans = min(ans, s)
    if not next_permutation(d): # 다음 순열이 없으면 끝
        break
print(ans)
