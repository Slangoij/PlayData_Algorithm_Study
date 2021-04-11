def solution(x):
    sticks = [2**i for i in range(7)]
    lght_lst = []
    
    for i in range(6,-1,-1):
        if sticks[i] <= x:
            lght_lst.append(x//sticks[i])
            x = x%sticks[i]
    
    return sum(lght_lst)

print(solution(48))