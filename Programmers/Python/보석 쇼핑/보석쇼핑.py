"""
Programmers 보석 쇼핑
Programmer: yooj
Date: 2021 09 11
Using: Python 3 & pycharm
Site: https://programmers.co.kr/learn/courses/30/lessons/67258
"""

def solution(gems):
    # 진열된 보석의 개수를 m 에 저장
    m = len(gems)
    # 자바나 c++ 의 맵과 같이 해당 스트링에 번호 부여
    q = dict()
    # 고유 번호를 부여하기 위해 사용한 변수
    pt = 0
    for i in range(m):
        # 키에 없을 경우 키 : 고유 번호로 매핑
        if gems[i] not in q.keys():
            q[gems[i]] = pt
            pt += 1
    # 총 사야하는 보석의 종류를 k 에 저장
    k = len(q.keys())
    # 현재 까지 산 보석의 개수를 저장할 배열
    c = [0] * k
    # 갖고있는 종류를 저장할 gen
    gen = 1
    # 투포인터를 위한 마지막
    en = 0
    # 해당 보석의 번호를 1 더해서 초기 값 설정
    c[q[gems[0]]] += 1
    # 산 보석의 시작과 끝을 -1 로 초기화
    start = -1
    end = -1
    for st in range(m):
        # 갖고있는 보석의 종류가 k 가 아니면 보석을 1개 더 구매한다.
        while gen != k and en < m:
            en += 1
            if en < m:
                # 갖고있는 개수가 0개인 보석을 사면 종류를 1개 추가
                if c[q[gems[en]]] == 0:
                    gen += 1
                # 해당 보석의 고유번호에 해당하는 c 값 1 증가
                c[q[gems[en]]] += 1
            # en 이 m 이 될 경우 끝
            if en == m:
                break
        if en == m:
            break
        # 갖고잇는 종류가 k 일 경우
        if gen == k:
            # -1 일 경우 값 설정
            if start == -1:
                start = st
                end = en
            else:
                # -1 이 아닐 경우 더 적은 개수를 사게 설정
                if end - start > en - st:
                    start = st
                    end = en
                # 만약 같을 경우 st가 낮은 쪽을 설정
                elif end - start == en - st:
                    if start > st:
                        start = st
                        end = en
        # 시작 인덱스의 보석을 1개 사지 않음
        c[q[gems[st]]] -= 1
        # 해당 인덱스가 0이 될 경우 갖고잇는 종류 1개 제거
        if c[q[gems[st]]] == 0:
            gen -= 1
    # index 가 아닌 1부터 시작해야 하므로 1씩 추가하여 답 출력
    return [start + 1, end + 1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
