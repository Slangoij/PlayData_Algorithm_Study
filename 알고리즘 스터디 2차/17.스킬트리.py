def solution(skill, skill_trees):
    answer = 0

    # 3rd try:
    idx_list = []

    for i in skill_trees:
        idx_list.clear()
        for j in skill:
            idx_list.append(i.find(j))

        while True:




        if not chk:
            return len(skill_trees)
        else:
            while len(idx_list) > 1 and idx_list[-1] == -1:
                del idx_list[-1]
            if idx_list[0] == -1:
                continue

            for k in range(len(idx_list)-1):
                if idx_list[k] > idx_list[k+1]:
                    break
                if k == len(idx_list)-2:
                    answer += 1

    return answer

    # # 2nd try: 스킬이 전체 미사용일때, 가능한 걸 고려 못함.
    # if len(skill) == 1:
    #     return len(skill_trees)
    # else:
    #     idx_list = []
    #
    #     for i in skill_trees:
    #         idx_list.clear()
    #         chk = False
    #         for j in skill:
    #             idx_list.append(i.find(j))
    #             if i.find(j) != -1:
    #                 chk = True
    #
    #         if not chk:
    #             return len(skill_trees)
    #         else:
    #             while len(idx_list) > 1 and idx_list[-1] == -1:
    #                 del idx_list[-1]
    #             if idx_list[0] == -1:
    #                 continue
    #
    #             for k in range(len(idx_list)-1):
    #                 if idx_list[k] > idx_list[k+1]:
    #                     break
    #                 if k == len(idx_list)-2:
    #                     answer += 1
    #
    # return answer



    # # 1st try: 사용되지 않은 스킬이 있는 경우 고려하지 못함
    # for i in skill_trees:
    #     tmp = -1
    #     chk = True
    #     for j in skill:
    #         if tmp < i.find(j):
    #             tmp = i.find(j)
    #         else:
    #             chk = False
    #             break
    #     if chk:
    #         answer += 1
    #
    # return answer


# skill = 'CBD'
# skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

skill = 'a'
skill_trees = ["bacd"]

print(solution(skill, skill_trees))