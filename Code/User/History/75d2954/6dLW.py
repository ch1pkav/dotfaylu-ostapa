v, e =  tuple(map(int, input().split()))
graph = {}
graph_w = {}
for i in range(e):
    start, end = tuple(map(int, input().split()))
    if start not in graph.keys():
        graph[start] = []
    graph[start].append(end)
    if end not in graph.keys():
        graph[end] = []
    graph[end].append(start)
    graph_w[(start, end)] = 0
    if (end,start) not in graph_w.keys():
        graph_w[(end, start)] = 1

cur_ver = 1
visited = set()
paths = [99999999]*v
paths[0] = 0
visited = set()
while cur_ver!=v:
    visited.add(cur_ver)
    minv = 99999999
    next_ver = None
    for vertex in graph[cur_ver]:
        if vertex not in visited:
            paths[vertex-1] = min(paths[vertex-1], paths[cur_ver] + graph_w[(cur_ver, vertex)])    
            if paths[vertex-1] < minv:
                minv = paths[vertex-1]
                next_ver = vertex
    if next_ver:
        cur_ver = next_ver
print(paths[-1])
