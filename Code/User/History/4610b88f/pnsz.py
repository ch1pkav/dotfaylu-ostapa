v, e = tuple(map(int, input().split()))
graph = {}
existing = []
weights = list(map(int, input().split()))
for i in range(e):
    existing.append(tuple(map(int, input().split())))
for i in range(v):
    for j in range(i+1, v):
        if (i+1, j+1) not in existing:
            graph[(i,j)] = weights[i] + weights[j]
        else:
            graph[(i,j)] = 0 

print(graph)
