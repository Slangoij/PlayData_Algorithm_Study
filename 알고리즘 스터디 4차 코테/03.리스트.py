def solution(A0, X, Y, M, n):
    a_lst = [A0]
    for i in range(n-1):
        a_lst.append((a_lst[i]*X+Y) % M)

    a_lst.sort()
    min_gap = 99999999
    for i in range(len(a_lst)-1):
        min_gap = min(min_gap, a_lst[i+1] - a_lst[i])

    return min_gap

# print(solution(1, 1221, 3553, 9889, 11))
print(solution(3, 7, 1, 101, 5))