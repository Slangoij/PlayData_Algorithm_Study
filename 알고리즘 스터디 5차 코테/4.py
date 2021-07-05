def solution(currentLanes):
    for i in range(len(currentLanes)):
        currentLanes[i] = list(currentLanes[i][::-1])

    if len(currentLanes[-1]) == 1:
        curchar = currentLanes.pop(-1)[0]
    else:
        curchar = currentLanes[-1].pop(-1)
    idx, leng = len(currentLanes), len(currentLanes)
    cnt = 1
    while curchar != 'D':
        if idx >= leng:
            idx = 0
        else:
            idx += 1

        if len(currentLanes[idx]) == 1:
            currentLanes.pop(idx)
            leng -= 1
        else:
            curchar = currentLanes[idx].pop()
        cnt += 1

    return cnt

currentLanes = ["AH","D","BCG","E","F"]
currentLanes = ["ABC","DEF"]
currentLanes = ["AB","CD","E"]
print(solution(currentLanes))
