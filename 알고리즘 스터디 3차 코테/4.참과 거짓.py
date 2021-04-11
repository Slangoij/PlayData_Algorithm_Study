def solution(statements):
    if sum(statements) not in range(len(statements)+1):
        return -1

    answer = 0
    for i in range(1,len(statements)+1):
        if statements.count(i) == i:
            answer = i

    return answer

print(solution([]))


# # 1st try: 가능한 답이 0개여도 -1 반환이 아닌 경우가 있???
# def solution(statements):
#     if sum(statements)==0:
#         return -1

#     answer = 0
#     leng = len(statements)
#     for i in range(1,leng+1):
#         if statements.count(i) == i:
#             answer = i

#     return answer