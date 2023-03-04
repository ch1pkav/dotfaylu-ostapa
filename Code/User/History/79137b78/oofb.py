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
paths = [-999999999] * len(graph.keys())
paths[0] = 1

for i in range (n-1):
    for edge in weights.keys():
        paths[edge[1]-1] = max(paths[edge[1]-1], paths[edge[0]-1]*weights[edge])
# while source != n:
#     mins = -99999999
#     next_ver = None
#     visited.add(source)
#     for vertex in graph[source]:
#         if vertex not in visited:
#             if weights[(source, vertex)] > paths[vertex-1]:
#                 paths[vertex-1] = paths[source-1] * weights[(source, vertex)]
#     for vertex in graph[source]:
#         if vertex not in visited:
#             if paths[vertex-1] > mins:
#                 mins = paths[vertex-1]
#                 next_ver = vertex
#     if next_ver:
#         source = next_ver
#         path.append(source)
# result = 1
# for i in range(len(path)-1):
    # result*=weights[(path[i], path[i+1])]

result=paths[-1]*100

print("%.6f percent" %result)
