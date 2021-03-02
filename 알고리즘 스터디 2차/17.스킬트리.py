# 다른 답안:
def solution(skill, skill_tree):
    answer = 0
    for i in skill_tree:
        skillist = ''
        for z in i:
            if z in skill:
                skillist += z
        if skillist == skill[:len(skillist)]:
            answer += 1
    return answer


skil = 'CBD'
skil_trees = ["BACDE", "CBADF", "AECB", "BDA"]

# skill = 'a'
# skill_trees = ["bacd"]

print(solution(skil, skil_trees))


# # 4th try:
# def solution(skill, skill_trees):
#     if len(skill) == 1:
#         return len(skill_trees)
#     else:
#         answer = 0
#         for i in skill_trees:
#             idx_list = []
#             for j in skill:
#                 idx_list.append(i.find(j))
#
#             if idx_list[0] == -1:
#                 if len(idx_list) and sum(idx_list) == -len(idx_list):
#                     answer += 1
#             else:
#                 last = len(idx_list)-1
#                 first = 0
#                 while last >= 0 and idx_list[last] == -1:
#                     last -= 1
#                 while first < len(idx_list) and idx_list[first] != -1:
#                     first += 1
#
#                 tmp_lst = idx_list[:last+1]
#                 if tmp_lst == sorted(tmp_lst) and last < first:
#                     answer += 1
#
#         return answer


# # 3rd try:
# def solution(skill, skill_trees):
#     answer = 0
#
#     for i in skill_trees:
#         idx_list = []
#         for j in skill:
#             idx_list.append(i.find(j))
#
#         if sum(idx_list) == -len(idx_list):
#             answer += 1
#         else:
#             if idx_list[0] == -1:
#                 break
#             else:
#                 tmp = -1
#                 chk = True
#                 for j in idx_list:
#                     if tmp < j:
#                         tmp = j
#                     elif tmp > j:
#                         chk = False
#                         if j == -1:
#                             tmp_j = idx_list.index(j, 1)
#                             tmp_lst = idx_list[tmp_j:]
#                             if sum(tmp_lst) == -len(tmp_lst):
#                                 answer += 1
#                         break
#
#         if chk:
#             answer += 1
#
#     return answer


# # 2nd try: 스킬이 전체 미사용일때, 가능한 걸 고려 못함.
# def solution(skill, skill_trees):
#     if len(skill) == 1:
#         return len(skill_trees)
#     else:
#         idx_list = []
#
#         for i in skill_trees:
#             idx_list.clear()
#             chk = False
#             for j in skill:
#                 idx_list.append(i.find(j))
#                 if i.find(j) != -1:
#                     chk = True
#
#             if not chk:
#                 return len(skill_trees)
#             else:
#                 while len(idx_list) > 1 and idx_list[-1] == -1:
#                     del idx_list[-1]
#                 if idx_list[0] == -1:
#                     continue
#
#                 for k in range(len(idx_list)-1):
#                     if idx_list[k] > idx_list[k+1]:
#                         break
#                     if k == len(idx_list)-2:
#                         answer += 1
#
#     return answer



# # 1st try: 사용되지 않은 스킬이 있는 경우 고려하지 못함
# def solution(skill, skill_trees):
#     for i in skill_trees:
#         tmp = -1
#         chk = True
#         for j in skill:
#             if tmp < i.find(j):
#                 tmp = i.find(j)
#             else:
#                 chk = False
#                 break
#         if chk:
#             answer += 1
#
#     return answer