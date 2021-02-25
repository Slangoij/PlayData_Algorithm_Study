import math

def solution(n):
    max_cnt = 0
    now_sum = 0
    for i in range(1, n + 1):
        if now_sum + i > n:
            break
        now_sum += i
        max_cnt += 1

    answer = 1
    nums_lst = [1]
    for i in range(2, max_cnt + 1):
        aftdiv = n / i
        if aftdiv - i/2 > 0:
            if ((i % 2) == 0 and aftdiv - math.floor(aftdiv) == 0.5)\
                    or ((i % 2) == 1 and aftdiv - int(aftdiv) == 0):
                nums_lst.append(i)
                answer += 1

    # print(n, nums_lst)
    return answer


for i in range(1, 101):
    print(solution(i))


    # for i in range(1, n + 1):
    #     if sum([_ for _ in range(1, i + 1)]) > n:
    #         break
    #
    #     aftdiv = n / i
    #     if not i % 2:
    #         if aftdiv - math.floor(aftdiv) == 0.5:
    #             answer += 1
    #     else:
    #         if aftdiv % 2 == 1:
    #             answer += 1

    # max_cnt = 0
    # tmp_sum = 0
    # for i in range(1, n):
    #     tmp_sum += i
    #     if tmp_sum > n:
    #         max_cnt = i
    #         break
    #
    # for i in range(max_cnt, 0, -1):
    #     for j in range(1, n - i + 2):
    #         now_lst = [_ for _ in range(j, j + i)]
    #         # print(now_lst)
    #         if sum(now_lst) == n:
    #             answer += 1
    #             print(now_lst)
    #             break