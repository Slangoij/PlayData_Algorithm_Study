def solution(n):
    answer = []
    nstr=str(n)
    for i in range(len(nstr)-1,-1,-1):
        answer.append(int(nstr[i]))
    return answer