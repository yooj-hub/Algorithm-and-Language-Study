'''
 * BOJ 오픈채팅방
 * programmer: yooj
 * using : pycharm & python 3.9.5
 * Date: 21.06.24
 * Site: https://programmers.co.kr/learn/courses/30/lessons/42888
'''


def solution(record):
    data = []
    for i in record:
        data.append(list(map(str, i.split())))#들어온 데이터를 분리하여 저장
    data2 = dict()#dict를 사용
    for i in data:
        if i[0] != "Leave":
            data2[i[1]] = i[2]#leave의 경우 이름이 명시되지 않고, 제일 마지막에 작성된 이름이 변경된 이름이므로 계속 갱신되게 작성
    ins = []
    for i in data:
        if i[0] != "Change":#change의 경우 따로 출력이 없음
            temp = data2[i[1]] + "님이"
            if i[0] == "Enter":#Enter인 경우
                temp += " 들어왔습니다."
            else:#Leave의 경우
                temp += " 나갔습니다."
            ins.append(temp)#완성된 문장을 ins 리스트에 저장

    return ins


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
