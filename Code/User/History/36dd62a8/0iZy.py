n, m = tuple(map(int, input().split()))
adj_list = [[]for i in range (n)]
edges = []
for i in range(m):
    a, b = tuple(map(lambda x: int(x)-1, input().split()))
    adj_list[a].append(b)
    adj_list[b].append(a)
    edges.append((a,b))

count = 0
#floud warshall based algorithm
distances = [[float("inf")for i in range(n)] for i in range(n)]
for edge in edges:
    distances[edge[0]][edge[1]] = 1
    distances[edge[1]][edge[0]] = 1
for i in range(n):
    distances[i][i] = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == 0 and k == n-1:
                if distances[j][k] <  distances[j][i] + distances[i][k]:
                    distances[j][k] = distances[j][i] + distances[i][k]
                    count = 0
                if distances[j][k] ==  distances[j][i] + distances[i][k]:
                    count+=1

print(count)



 
