def solution(n):
    answer = 0
    if not n:
        return n
    else:
        for i in list(range(1,n+1)):
            if not (n%i):
                answer+=i
    return answer