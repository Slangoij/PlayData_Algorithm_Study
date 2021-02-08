def solution(s):
    leng=len(s)
    if leng%2:
        answer=s[int(leng/2)]
    else:
        answer=s[int(leng/2)-1:int(leng/2)+1]
    return answer