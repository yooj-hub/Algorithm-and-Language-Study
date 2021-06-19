def solution(numbers):
    key=0
    for i in range(len(numbers)-1):
        if numbers[i]!=numbers[i+1]:
            key+=1
    if numbers[0]==numbers[-1]:
        return key//2
    else:
        return key//2+1

data=input()
print(solution(data))