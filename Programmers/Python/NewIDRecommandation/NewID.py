'''
 * Programmers 신규 아이디 추천
 * programmer: yooj
 * using : pycharm & python 3.9.5
 * Date: 21.06.27
 * Site: https://programmers.co.kr/learn/courses/30/lessons/72410
'''


def solution(new_id):
    #1단계
    new_id = new_id.lower()
    print(new_id)
    ans = ""
    #2단계
    for i in new_id:
        if i.isalpha() or i.isdigit() or i == "-" or i == "_" or i == ".":
            ans += i
    ans = removeDot(ans)#3단계
    ans = removeStartEndDot(ans)#4단계
    #5단계
    if ans == "":
        ans += "a"
    #6단계
    if len(ans) > 15:
        ans = ans[:15]
        ans = removeStartEndDot(ans)
    #7단계
    if len(ans) < 3:
        k = 3 - len(ans)
        for i in range(k):
            ans += ans[len(ans) - 1]

    return ans

#3단계 재귀로 구현
def removeDot(new_id):
    if new_id.__contains__(".."):
        new_id = new_id.replace("..", ".")
        return removeDot(new_id)
    else:
        return new_id

#4단계 재귀를 통한 구현
def removeStartEndDot(new_id):
    n = len(new_id)
    if new_id[0] == ".":
        if n>=2:
            new_id = new_id[1:]
            return removeStartEndDot(new_id)
        else:
            return ""
    if new_id[n - 1] == ".":
        new_id = new_id[:n - 1]
        return removeStartEndDot(new_id)
    return new_id


print(solution(	"abcdefghijklmn.p"))
