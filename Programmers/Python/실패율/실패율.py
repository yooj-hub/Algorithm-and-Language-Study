def solution(N: int, stages: [int]):
    answer = []
    d = [0] * (N + 2)
    f = [0] * (N + 2)
    for i in stages:
        for j in range(1, i + 1):
            d[j] += 1
        f[i] += 1
    tmp = []
    for i in range(1, N + 1):
        if d[i] != 0:
            tmp.append((f[i] / d[i], i))
        else:
            tmp.append((0, i))
    tmp.sort(key=lambda x: (-x[0], x[1]))
    for i in tmp:
        answer.append(i[1])
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
