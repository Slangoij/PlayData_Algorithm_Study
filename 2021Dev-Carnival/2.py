# 2개의 유닛을 동시에 같은 방향으로 움직여 도착지점에 보내는 문제
# 장애물: 'X' 이 있으면 막힌 유닛만 이동하지 못하고 이동할 수 있는 유닛은
# 그대로 이동 가능
# 도착할 수 있는 방법이 없으면 -1 출력

from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))

tmp_input = list(map(int, input().split()))
que = deque((tmp_input[0],tmp_input[1]), (tmp_input[2],tmp_input[3]))
answer = 0
while que:
    unit1 = que.popleft()
    unit2 = que.popleft()

    x1, y1, x2, y2, = 0, 0, 0, 0
    for dir in [[0,-1],[0,1],[1,0],[-1,0]]:
        x1 = unit1[0]+dir[0], y1 = unit1[1]+dir[1]
        if graph[x1][y1] == 'D':
            continue
        if x1 in range(n) and y1 in range(n) and graph[x1][y1] != 'X':
            que.append((x1,y1))

        x2 = unit2[0]+dir[0], y2 = unit2[1]+dir[1]
        if graph[x2][y2] == 'D':
            continue
        if x2 in range(n) and y2 in range(n) and graph[x2][y2] != 'X':
            que.append((x2,y2))

    answer += 1

print()