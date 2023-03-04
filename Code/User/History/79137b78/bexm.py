n, m = tuple(map(int, input().split()))
weights = {}
for i in range(m):
    x,y,t = tuple(map(int, input().split()))
    weights[(x,y)]= t/100
    weights[(y,x)]= t/100
paths = [float("-inf") for _ in range(n)]
paths[0] = 1
for i in range (n-1):
    for edge in weights.keys():
        paths[edge[1]-1] = max(paths[edge[1]-1], paths[edge[0]-1]*weights[edge])
result=paths[-1]*100
print("%.6f percent" %result)