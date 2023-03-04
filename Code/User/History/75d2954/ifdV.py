v, e =  tuple(map(int, input().split()))
graph_w = {}
for i in range(e):
    start, end = tuple(map(int, input().split()))
    graph_w[(start, end)] = 0
    if (end,start) not in graph_w.keys():
        graph_w[(end, start)] = 1

paths = [99999999]*v
paths[0] = 0

for i in range (v-1):
    for edge in graph_w.keys():
        paths[edge[1]-1] = min(paths[edge[1]-1], paths[edge[0]-1]+graph_w[edge])

print(paths[-1])

