def solution(n):
    return len( [i for i in range(1, n + 1, 2) if n % i == 0] )


print(solution(15))