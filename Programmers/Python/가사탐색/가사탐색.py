# /*
#  * Programmers 가사 탐색
#  * programmer: yooj
#  * Date: 21.07.21
#  * using: Pycharm  & Python3
#  * Site: https://www.acmicpc.net/problem/14501
#  */

import bisect


def solution(words, queries):
    answer = []
    d = [[] for _ in range(10001)]  # 단어를 길이별로 저장할 배열
    rd = [[] for _ in range(10001)] # 거꾸로 적은 단어를 길이별로 저장할 배열
    for i in words:
        d[len(i)].append(i)
        rd[len(i)].append(i[::-1])
    for i in range(10001):
        d[i].sort()  # 이진 탐색을 사용하기 위한 정렬
        rd[i].sort()
    for j in range(len(queries)): # 모든 쿼리에 대한 탐색
        length = len(queries[j])
        # 맨 처음이 ? 가아닌 경우를 이진 탐색 하여 개수 구하기
        if queries[j][0] != '?':
            target = queries[j].replace('?', 'a')
            left = bisect.bisect_left(d[length], target)
            target = queries[j].replace('?', 'z')
            right = bisect.bisect_right(d[length], target)
            answer.append(right - left)
        # 맨 처음이 ? 인 경우를 이진 탐색 하여 개수 구하기
        else:
            target = queries[j].replace('?', 'a')
            left = bisect.bisect_left(rd[length], target[::-1])
            target = queries[j].replace('?', 'z')
            right = bisect.bisect_right(rd[length], target[::-1])
            answer.append(right - left)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
