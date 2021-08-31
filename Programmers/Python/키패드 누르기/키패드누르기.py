"""
Programmers 키패드 누르기
Programmer: yooj
Date: 2021 08 31
Using: Python 3 & pycharm
Site: https://programmers.co.kr/learn/courses/30/lessons/67256
"""

import copy


def solution(numbers: [int], hand: str):
    right = False
    answer = ''
    #  오른손 잡이인지 확인 ( 오른손 잡이가 아닐 경우 무조건 왼손잡이 이므로 오른손 잡이인지만 확인)
    if hand == "right":
        right = True
    #  처음 위치 설정
    rightPos = getPosition("*")
    leftPos = getPosition("#")
    for i in numbers:
        # 1 , 4, 7 인 경우 왼손으로 입력 후 위치를 해당 번호로 이동
        if i in [1, 4, 7]:
            leftPos = getPosition(i)
            answer += "L"
        # 3 , 6, 9 인 경우 왼손으로 입력 후 위치를 해당 번호로 이동
        elif i in [3, 6, 9]:
            rightPos = getPosition(i)
            answer += "R"
        # 나머지 번호의 경우
        else:
            # 목표 지점을 구한다.
            target = getPosition(i)
            # 왼쪽과 목표지점 사이의 거리를 구함
            leftDist = getDist(leftPos, target)
            # 오른쪼고가 목표지점 사이의 거리를 구함
            rightDist = getDist(rightPos, target)
            # 거리가 같은 경우
            if leftDist == rightDist:
                # 오른손 잡이 일 경우 오른손으로 처리
                if right:
                    rightPos = copy.deepcopy(target)
                    answer += "R"
                # 왼손 잡이 일 경우 왼손으로 처리
                else:
                    leftPos = copy.deepcopy(target)
                    answer += "L"
            # 거리가 다른 경우 거리가 짧은 쪽으로 입력후 그 손을 옮김
            elif leftDist < rightDist:
                leftPos = copy.deepcopy(target)
                answer += "L"
            else:
                rightPos = copy.deepcopy(target)
                answer += "R"

    return answer


# cur 을 이용하여 4 * 3 배열에 맞는 위치를 반환하는 함수
def getPosition(cur):
    if cur == "*":
        cur = 10
    elif cur == "#":
        cur = 12
    elif cur == "0" or cur == 0:
        cur = 11
    else:
        cur = int(cur)
    cur -= 1
    return [cur // 3, cur % 3]


# 거리를 구하는 함수
def getDist(f, t):
    return abs(f[0] - t[0]) + abs(f[1] - t[1])


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
