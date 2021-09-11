def solution(weights, head2head):
    answer = []
    n = len(weights)
    a = []
    for i in range(n):
        data = [i, 0.0, 0, weights[i]]  # 번호, 승률, 무거운애, 몸무게
        cnt = 0
        win = 0
        heavyCnt = 0
        for j in range(n):
            if head2head[i][j] == "W":
                win += 1
                cnt += 1
                if weights[i] < weights[j]:
                    heavyCnt += 1
            if head2head[i][j] == "L":
                cnt += 1
        if cnt != 0:
            data[1] = win / cnt
        data[2] = heavyCnt
        a.append(data)

    a.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))
    for i in range(n):
        answer.append(a[i][0] + 1)
    return answer


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
