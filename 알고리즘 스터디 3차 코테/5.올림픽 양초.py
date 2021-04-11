def solution(candles):
    day = 1
    while True:
        candles.sort(reverse=True)
        for i in range(day):
            candles[i] -= 1
        while candles.count(0):
            candles.remove(0)
        if len(candles) <= day:
            break
        day += 1

    return day

print(solution([5,2,2,1]))