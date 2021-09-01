def solution(str1: str, str2: str):
    tmp1 = []
    tmp2 = []
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1) - 1):
        s = [str1[i:i + 2]]
        if s[0][0].isalpha() and s[0][1].isalpha():
            tmp1 += s
    for i in range(len(str2) - 1):
        s = [str2[i:i + 2]]
        if s[0][0].isalpha() and s[0][1].isalpha():
            tmp2 += s
    if len(tmp1) == 0 and len(tmp2) == 0:
        return 65536
    s = len(tmp1) + len(tmp2)
    visited = [False] * len(tmp2)
    p = 0
    for i in tmp1:
        for j in range(len(tmp2)):
            if i == tmp2[j] and not visited[j]:
                p += 1
                visited[j] = True
                break
    answer = p * 65536 // (s - p)
    return answer


str1 = "aa1+aa2"
str2 = "	AAAA12"
print(solution(str1, str2))
