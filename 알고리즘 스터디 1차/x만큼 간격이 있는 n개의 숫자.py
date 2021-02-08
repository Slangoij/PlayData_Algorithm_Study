def solution(x, n):
    answer = []
    tmp=x
    for i in range(0,n):
        answer.append(tmp)
        tmp+=x
    return answer