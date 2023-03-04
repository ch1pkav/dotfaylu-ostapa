n, m = tuple(map(int, input().split()))
singles = []
graph = []
for i in range(m):
    x = input.split()
    is_single = x[0] == "S"
    edge = list(map(int, x[1:]))
    graph.append(edge)
    singles.append(is_single)

