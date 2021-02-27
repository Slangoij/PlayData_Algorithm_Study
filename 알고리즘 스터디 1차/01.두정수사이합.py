def solution(a, b):
    if not (a-b):
        return a
    elif (a-b)<0:
        lst=range(a,b+1)
    else:
        lst=range(b,a+1)
    return sum(lst)