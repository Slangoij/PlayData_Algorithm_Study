def solution(people, limit):
    # 3rd try:
    leng = len(people)
    answer = leng

    people.sort(reverse=True)

    for i in range(leng-1):
        if people[i]+people[-1] <= limit:
            break

    j = len(people)-1
    while i < j:
        if people[i]+people[j] <= limit:
            j -= 1
            answer -= 1
        i += 1

    return answer




    # # 2dn try:
    # leng = len(people)
    # answer = leng
    #
    # chk = [False for _ in range(leng)]
    # for i in range(leng):
    #     for j in range(i+1, leng):
    #         if not chk[i] and not chk[j] and people[i]+people[j] <= limit:
    #             chk[i] = chk[j] = True
    #             answer -= 1
    #
    # return answer

    # # 1st try:
    # while True:
    #     chk = False
    #     for i in range(len(people)):
    #         chk1 = False
    #         for j in range(i+1,len(people)):
    #             if people[i]+people[j] <= limit:
    #                 answer += 1
    #                 people.pop(j)
    #                 people.pop(i)
    #                 chk = chk1 = True
    #                 break
    #         if chk1:
    #             break
    #     if not chk:
    #         break
    #
    # answer += len(people)
    #
    # return answer


people = [70, 50, 80, 50]
limit = 100

# people = [70, 80, 50]
# limit = 100

print(solution(people, limit))