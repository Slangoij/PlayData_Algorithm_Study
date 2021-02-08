# 2nd try:
def solution(A, B):
    answer = 0

    A.sort()
    B.sort()
    A.reverse()

    for t_a, t_b in zip(A, B):
        answer += t_a * t_b

    return answer

# # 1st try:
# from itertools import combinations, permutations
# import sys

#
#     a_permu = permutations(A)
#     b_permu = permutations(B)

#     sums = sys.maxsize
#     for i in a_permu:
#         for j in b_permu:
#             t_sum = 0
#             for (t_a, t_b) in zip(i, j):
#                 t_sum += t_a * t_b
#             sums = min(sums, t_sum)

#     return sums