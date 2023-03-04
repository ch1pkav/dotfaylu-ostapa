v, e = tuple(map(int, input().split()))
graph = {}
existing = []
weights = list(map(int, input().split()))
for i in range(e):
    ed = tuple(map(lambda x: int(x)-1, input().split()))
    graph[ed] = 0
# for i in range(v):
#     for j in range(i+1, v):
#         if (i, j) not in existing and (j, i) not in existing:
#             graph[(i,j)] = weights[i] + weights[j]
#             # graph[(j,i)] = weights[i] + weights[j]
#         else:
#             graph[(i,j)] = 0 
#             # graph[(j,i)] = 0

sets = [{i} for i in range(v)]
graph  = dict(sorted(graph.items(), key = lambda x: x[1]))
tree=[]
for verx in graph:
    l=0
    l_copy= 0
    reserved_1 = []
    for i in range(len(sets)):
        if (verx[0] in sets[i] and verx[1] not in sets[i]) or (verx[0] not in sets[i] and verx[1] in sets[i]):
            reserved_1.append(sets[i])
            sets[i] = set()
            if len(reserved_1) == 2:
                sets[i] = reserved_1[0].union(reserved_1[1])
                l = 1
                break
    if l != l_copy:
        tree.append(verx)
    if len(tree)==(len(sets)-1):
        break
while set() in sets:
    sets.remove(set())
print(sets)
min_for_component=[]
for component in sets:
    min_cost = 99999999
    for vertex in component:
        min_cost = min(min_cost, weights[vertex])
    min_for_component.append(min_for_component)
smallest = min(min_for_component)
min_for_component.remove(smallest)
result = 0
for component in min_for_component:
    result+= smallest+component
print(result)
# print(existing)
# print(graph)
# print(tree)
# result = 0
# for edge in tree:
#     result+= graph[edge]
# print(result)
