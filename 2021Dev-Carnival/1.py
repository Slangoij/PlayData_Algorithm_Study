n, k = map(int, input().split())

lst = list(map(int, input().split()))

food_lst = list(set(lst))
idxed_lst = [(idx+1, food, (idx-k+1)%n) for idx, food in enumerate(lst)]

idxed_lst.sort(key=lambda x: (x[1], x[-1]))

answer = [i[0] for i in idxed_lst]
for ans in answer:
    print(ans, end=' ')