def solution(n):
    answer = ''
    for i in range(0,n):
        if i%2:
            answer+='박'
        else:
            answer+='수'
    return answer