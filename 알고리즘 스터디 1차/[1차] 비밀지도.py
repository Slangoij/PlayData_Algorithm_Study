def solution(n, arr1, arr2):
    answer = []

    for i in zip(arr1, arr2):
        bin_fir = int(bin(i[0]), 2)
        bin_sec = int(bin(i[1]), 2)
        tmp = bin(bin_fir | bin_sec)

        nowstr = tmp[-n:]
        leng = len(nowstr)
        str_result = ''
        for j in range(0, leng):
            if nowstr[j] == '1':
                str_result += '#'
            else:
                str_result += ' '

        answer.append(str_result)

    return answer