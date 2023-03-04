n, m = tuple(map(int, input().split()))
graph = {}
weights = {}
for i in range(m):
    x, y, t = tuple(map(int, input().split()))
    if (x,y) in weights.keys():
        weights[(x,y)] = min(t,  weights[(x,y)])
    else:
        weights[(x,y)] = t
    if x not in graph.keys():
        graph[x] = []
    graph[x].append(y)

visited = []
cur_path = []
stack = []
stack.append(0)
cycles = []
go_next = True
loopexit = False
while stack:
    vertex = stack.pop()
    if not loopexit:
        cur_path.append(vertex)
        if vertex in visited:
            starting = cur_path.index(vertex)
            if cur_path[starting:] not in cycles:
                sum = 0
                for i in range(starting, len(cur_path)-1):
                    if (cur_path[i], cur_path[i+1]) in weights.keys():
                        sum += weights[cur_path[i], cur_path[i+1]]
                if sum < 0:
                    print("possible")
                    go_next = False
            else:
                loopexit = True
            cycles.append(cur_path[starting:])
            cur_path = []
            visited = []
            cur_path.append(vertex)
        visited.append(vertex)
        if go_next:
            if vertex in graph.keys():
                for ver in graph[vertex]:
                    stack.append(ver)
    
if go_next:
    print("not possible")

