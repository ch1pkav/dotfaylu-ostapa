n, m = tuple(map(int, input().split()))
graph = {}
weights = {}
for i in range(m):
    x, y, t = tuple(map(int, input().split()))
    weights[(x,y)] = t 
    if x not in graph.keys():
        graph[x] = []
    else:
        graph[x].append(y)

visited = []
cur_path = []
stack = []
stack.append(0)
go_next = True
while stack:
    vertex = stack.pop()
    cur_path.append(vertex)
    if vertex in visited:
        sum = 0
        for i in range(len(cur_path)-1):
            sum += weights[cur_path[i], cur_path[i+1]]
        if sum < 0:
            print("possible")
            go_next = False
        cur_path = []
    visited.append(vertex)
    if go_next:
        for ver in graph[vertex]:
            stack.append(ver)
    
if go_next:
    print("not possible")

