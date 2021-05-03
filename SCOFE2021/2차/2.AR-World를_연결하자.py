import heapq

N = int(input())

citylst = []
for _ in range(N):
    tmp_lst = input().split()
    tmp_lst.sort()
    citylst.append(tmp_lst[1])
    citylst.append(tmp_lst[2])

citylst = list(set(citylst))
M = len(citylst)
vstd = [False] * M
costarr = [[0]*M for _ in range(M)] 

for _ in range(N):
    tmp_lst = input().split()
    tmp_lst.sort()
    costarr[citylst.index(tmp_lst[1])][citylst.index(tmp_lst[2])] = tmp_lst[0]

def dfs()






# def dicks(graph, start):
#   dists = {node: float('inf') for node in graph}
#   dists[start] = 0
#   queue = []
#   heapq.heappush(queue, [dists[start], start])

#   while queue:
#     current_distance, current_destination = heapq.heappop(queue)

#     if dists[current_destination] < current_distance:
#       continue
    
#     for new_destination, new_distance in graph[current_destination].items():
#       distance = current_distance + new_distance
#       if distance < dists[new_destination]:
#         dists[new_destination] = distance
#         heapq.heappush(queue, [distance, new_destination])
    
#   return dists

# graph = {}
# for _ in range(N):
#     tmplst = input().split()
#     tmplst.sort()
#     tmpdic = {}
#     tmpdic[tmplst[1]] = tmplst[0]
#     graph[tmplst[2]] = tmpdic

# to_str = graph.keys()[0]
# distss = diks(graph, to_str)
# anslst = sorted(distss.items(), key=lambda x: x[1])
# print(anslst[1][1])