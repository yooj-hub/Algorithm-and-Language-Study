def solution(dartResult: str):
    stk = []
    t = ""
    for i in dartResult:
        if i.isdigit():
            t += i
        elif i.isalpha():
            k = 0
            if i == "S":
                k = 1
            elif i == "D":
                k = 2
            else:
                k = 3
            stk.append(int(t) ** k)
            t=""
        else:
            if i == "*":
                if len(stk) > 1:
                    stk[-1] = stk[-1] * 2
                    stk[-2] = stk[-2] * 2
                else:
                    stk[-1]=stk[-1]*2
            else:
                stk[-1] = -stk[-1]

    answer = sum(stk)
    return answer


print(solution("1D2S#10S"))
