v, e = tuple(map(int, input().split()))
graph = [[]for _ in range(v)]
existing = []
weights = list(map(int, input().split()))
minval = min(weights)
for i in range(e):
    start, end = tuple(map(lambda x: int(x)-1, input().split()))
    graph[start].append(end)
    graph[end].append(start)

stack = []
def dfs(vertex, graph, weights):
    minv = 99999999999
    stack = []
    stack.append(vertex)
    # visited[vertex] = True
    while(stack):
        vertex= stack.pop()
        minv = min(minv, weights[vertex])
        # if not(visited[vertex]):
        for v in graph[vertex]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True
    return minv
    

sum = 0
iters = 0
visited = [False for i in range(v)]
for ind, w in enumerate(weights):
    if not visited[ind]:
        sum += dfs(ind, graph, weights)
        iters+=1

sum+=(iters-2)*minval

# result = 0
# minval = min(minimals)
# minimals.remove(minval)
# for component in minimals:
#     result+=(minval+component)
print(sum)
