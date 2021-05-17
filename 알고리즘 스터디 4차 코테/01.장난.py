def solution(apparentGain):
    answer = []
    for i in range(1,1000):
        for j in range(1,i):
            if i**2 - j**2 == apparentGain:
                answer.append(i)

    return answer
    
# print(solution(233))
# print(solution(15))
print(solution(1440))
# for i in range(100001):
#     print(i, solution(i))