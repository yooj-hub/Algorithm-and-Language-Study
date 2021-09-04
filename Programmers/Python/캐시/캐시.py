def solution(cacheSize, cities):
    answer = 0
    c = [""] * cacheSize
    p = 0
    count = [-1] * cacheSize
    if cacheSize == 0:
        return len(cities) * 5
    for i in range(len(cities)):
        s = cities[i].lower()
        if s in c:
            count[c.index(s)] = i
            answer += 1
        else:
            if p < cacheSize:
                c[p] = s
                count[p] = 1
                p += 1
                answer += 5
            else:
                idx = 0
                cmp = count[0]
                for j in range(1, len(count)):
                    if cmp > count[j]:
                        cmp = count[j]
                        idx = j
                c.pop(idx)
                count.pop(idx)
                c.append(s)
                count.append(i)
                answer += 5

    return answer


print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
