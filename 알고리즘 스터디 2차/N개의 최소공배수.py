def get_chso(a, b):
    if a == 1:
        return b
    else:
        r_a = a
        r_b = b
        tmp = 0
        while b % a != 0:
            tmp = a
            a = b % a
            b = tmp

        return (r_a * r_b) / a


def solution(arr):
    answer = 1

    com_arr = arr
    com_arr.sort()

    for i in com_arr:
        answer = get_chso(answer, i)
    return answer