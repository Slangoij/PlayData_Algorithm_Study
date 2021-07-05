def solution(signs):
    cnt = 0
    if signs[-1] != 'default' and signs[-1] != 'city':
        return int(signs[-1])

    for sign in signs:
        if sign == 'city':
            cnt += 1
    
    if cnt%2==0:
        return 60
    return 90