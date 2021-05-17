def solution(diet, breakfast, lunch):
    for i in breakfast:
        if i not in diet:
            return "CHEATER"
        diet = diet.replace(i, '')
        
    for i in lunch:
        if i not in diet:
            return "CHEATER"
        diet = diet.replace(i, '')

    diet_lst = list(diet)
    diet_lst.sort()
    return ''.join(diet_lst)

diet = "ABEDCS"
breakfast = ''
lunch = ''

print(solution(diet, breakfast, lunch))