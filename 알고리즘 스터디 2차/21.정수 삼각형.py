def solution(triangle):

    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j:
                triangle[i][j] += triangle[i-1][j-1]
            if not j:
                triangle[i][j] += triangle[i-1][j]
            elif j < i and triangle[i-1][j-1] < triangle[i-1][j]:
                triangle[i][j] += triangle[i-1][j] - triangle[i-1][j-1]

    return max(triangle[-1])

trianglee = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(trianglee))