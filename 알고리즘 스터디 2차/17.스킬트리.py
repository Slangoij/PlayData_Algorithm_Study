def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        tmp = -1
        chk = True
        for j in skill:
            if tmp < i.find(j):
                tmp = i.find(j)
            else:
                chk = False
                break
        if chk:
            answer += 1

    return answer


skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))