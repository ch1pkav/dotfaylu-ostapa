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
def dfs(vertex, visited, graph, weights):
    minv = 99999999999
    stack = []
    stack.append(vertex)
    # visited[vertex] = True
    while(stack):
        vertex= stack.pop()
        minv = min(minv, weights[vertex])
        if not(vertex in visited):
            visited.add(vertex)
        for v in graph[vertex]:
            if not (v in visited):
                stack.append(v)
    return minv, visited
    

sum = 0
iters = 0
# visited = [False for i in range(v)]
visited = set()
for ind, w in enumerate(weights):
    if not( w in visited):
        sum += dfs(ind, visited, graph, weights)
        iters+=1

sum+=(iters-2)*minval

# result = 0
# minval = min(minimals)
# minimals.remove(minval)
# for component in minimals:
#     result+=(minval+component)
print(sum)



# sets = [{i} for i in range(v)]
# graph  = dict(sorted(graph.items(), key = lambda x: x[1]))
# for verx in graph:
#     l=0
#     l_copy= 0
#     reserved_1 = []
#     for i in range(len(sets)):
#         if (verx[0] in sets[i] and verx[1] not in sets[i]) or (verx[0] not in sets[i] and verx[1] in sets[i]):
#             reserved_1.append(sets[i])
#             sets[i] = set()
#             if len(reserved_1) == 2:
#                 sets[i] = reserved_1[0].union(reserved_1[1])
#                 l = 1
#                 break
# while set() in sets:
#     sets.remove(set())
# # print(sets)
# min_for_component=[]
# for component in sets:
#     min_cost = 99999999
#     for vertex in component:
#         min_cost = min(min_cost, weights[vertex])
#     min_for_component.append(min_cost)
# smallest = min(min_for_component)
# min_for_component.remove(smallest)
# result = 0
# for component in min_for_component:
#     result+= smalles
# t+component
# print(result)
# print(existing)
# print(graph)
# print(tree)
# result = 0
# for edge in tree:
#     result+= graph[edge]
# print(result)
