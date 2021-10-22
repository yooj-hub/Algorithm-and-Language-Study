import sys

n = int(sys.stdin.readline())
# 같은 칼럼에 퀸이 존재하는지 확인하는 flag
flag_b = [False] * n
# / 방향의 대각선에 퀸이 존재하는지 확인하는 flag
flag_c = [False] * (n + n - 1)
# \ 방향의 대각선에 퀸이 존재하는지 확인하는 flag
flag_d = [False] * (n + n - 1)


# 백트랙킹을 이용한 정답 찾기
# 이미 같은 row 에 있을 경우 검사하지 않고 다음으로 가기 위해 row 를 변수로 받음
def dfs(row):
    answer = 0
    if row == n:
        return 1
    for j in range(n):
        # 존재 유무 체크
        if flag_b[j] or flag_c[row + j] or flag_d[row - j + n - 1]:
            continue
        else:
            changeFlag(row, j, True)
            answer += dfs(row + 1)
            changeFlag(row, j, False)
    return answer


# flag 값을 check 로 바꾸는 함수
def changeFlag(i, j, check):
    flag_b[j] = check
    flag_c[i + j] = check
    flag_d[i - j + n - 1] = check


print(dfs(0))
