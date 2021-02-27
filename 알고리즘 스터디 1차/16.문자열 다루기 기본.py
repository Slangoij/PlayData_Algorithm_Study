def solution(s):
    answer = True
    leng=len(s)
    if leng!=4&leng!=6:
        answer=False
    if not s.isdigit():
        answer=False
    return answer