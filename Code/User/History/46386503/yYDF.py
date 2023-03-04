n, m = tuple(map(int, input().split()))
singles = []
edges = []
graph = [[]for _ in range(n)]
result = "1"

def dfs(ver):
    stack = []
    stack.append(ver)
    while stack:
        s = stack.pop()
        for adj in graph[ver]:
            stack.append(adj)
            visited[adj] = True
    


for i in range(m):
    x = input().split()
    is_single = x[0] == "S"
    edge = list(map(lambda y: int(y)-1, x[1:]))
    edges.append(edge)
    singles.append(is_single)

visited = [False for _ in range (n)]
components = 0
for vertex in range(n):
    if not visited[vertex]:
        dfs(visited)
        components+=1

print(bin(components))

# for vertex in edges:
#     graph[vertex[0]].append(vertex[1])
#     graph[vertex[1]].append(vertex[0])

# for ind, state in enumerate(singles):
#     if state:
#         graph[edges[ind][0]].remove(edges[ind][1])
#         graph[edges[ind][1]].remove(edges[ind][0])
#         graph[edges[ind][0]] += graph[edges[ind][1]]
#         graph.pop(edges[ind][1])
#         graph = [[graph[i][j] if graph[i][j] != edges[ind][1] else edges[ind][0] for j in range(len(graph[i]))]for i in range(len(graph))]

# print(graph)

# def bfs():
#     pass

        

