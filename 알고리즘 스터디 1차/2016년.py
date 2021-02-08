def solution(a, b):
    answer = ''
    lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    tot_days = sum(lst[0:a - 1]) + (b - 1)
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

    answer = days[(tot_days + 5) % 7]

    return answer