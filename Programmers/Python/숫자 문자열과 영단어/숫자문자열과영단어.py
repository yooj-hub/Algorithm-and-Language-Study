numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solution(s: str):
    t = ""
    ans = []
    for i in s:
        if i.isdigit():
            ans.append(i)
        else:
            t += i
        if t in numbers:
            ans.append(numbers.index(t))
            t = ""

    answer = int(''.join(map(str, ans)))
    return answer


print(solution("one4seveneight"))
