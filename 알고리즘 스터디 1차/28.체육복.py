def solution(n, lost, reserve):
    answer = 0

    set_l = set(lost)
    set_r = set(reserve)
    set_all = {i for i in range(1, n + 1)}

    lft_los = set_l - set_r
    lft_res = set_r - set_l
    set_all = set_all - lft_los

    for i in lft_los:
        i_plus = i + 1
        i_minus = i - 1
        if i_minus in lft_res:
            lft_res.remove(i_minus)
            set_all.add(i)
        elif i_plus in lft_res:
            lft_res.remove(i_plus)
            set_all.add(i)

    for i in lft_res:
        if not i in set_all:
            set_all.add(i)
            lft_res.remove(i)

    return len(set_all)

    #     left=[1 for _ in range(0,n+1)]

    #     for i in lost:
    #         left[i] -= 1

    #     for i in reserve:
    #         if left[i] == 0:
    #             left[i] += 1
    #             reserve.remove(i)

    #     for i in reserve:
    #         if i>1 and not left[i-1]:
    #             left[i-1] += 1
    #     for i in reserve:
    #         if i<n and not left[i+1]:
    #             left[i+1] += 1
    #         reserve.remove(i)

    #     for i in range(1,n+1):
    #         if left[i]:
    #             answer += 1

    return answer