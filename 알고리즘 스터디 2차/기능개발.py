import math

def solution(progresses, speeds):
    answer = []

    nlist = []
    for i, j in zip(progresses, speeds):
        nlist.append(math.ceil((100 - i) / j))

    tmp = 1
    tmp_max = nlist[0]
    for i in range(1,len(nlist)):
        if tmp_max < nlist[i]:
            answer.append(tmp)
            tmp = 1
            tmp_max = nlist[i]
        else:
            tmp += 1
    if tmp:
        answer.append(tmp)

    return answer

# progresses = [93, 30, 55]
# speeds = [1, 30, 5]

progresses = [98, 98,98,98,98, 97,96]
speeds = [1, 2,1,2,1,1,1]

print(solution(progresses,speeds))