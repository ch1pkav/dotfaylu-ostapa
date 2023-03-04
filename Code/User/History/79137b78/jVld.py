n, m = tuple(map(int, input().split()))
graph = {}
weights = {}
for i in range(m):
    x,y,m = tuple(map(int, input().split()))
    if x not in graph.keys():
        graph[x] = []
    if y not in graph.keys():
        graph[y] = []
    graph[x].append(y)
    graph[y].append(x)
    weights[(x,y)]= m/100
    weights[(y,x)]= m/100

source = 1
paths = [9999999] * len(graph.keys())
visited = set()
paths[0] = 1
while source != n:
    mins = -99999999
    next_ver = None
    visited.add(source)
    for vertex in graph[source]:
        if vertex not in visited:
            if weights[(source, vertex)] < paths[vertex-1]:
                paths[vertex-1] = paths[source-1] * weights[(source, vertex)]
    for vertex in graph[source]:
        if paths[vertex-1] > mins:
            mins = paths[vertex-1]
            next_ver = vertex
    if next_ver:
        source = next_ver
print(paths[-1])
