def solution(s: str):
    answer = 0
    if len(s) == 1:
        return 1
    for length in range(1, len(s) // 2 + 1):
        t = ""
        tmp = ""
        cnt = 1
        k = 0
        for j in range(0, len(s) - length + 1, length):
            k = j + length
            if t == s[j:j + length]:
                cnt += 1
            elif t != s[j:j + length] and t != "":
                if cnt == 1:
                    tmp += t
                else:
                    tmp += str(cnt) + t
                t = ""
            if t == "":
                cnt = 1
                t = s[j:j + length]
        if cnt == 1:
            tmp += t
        else:
            tmp += str(cnt) + t
        for x in range(k, len(s)):
            tmp += s[x]
        if answer == 0 or answer > len(tmp):
            answer = len(tmp)
    return answer


print(solution("a"))
