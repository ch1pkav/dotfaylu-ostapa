points = []
n = int(input())
for i in range (n):
    points.append(tuple(map(int, input().split())))

for point in points:
    on_x = list(filter(lambda x: x[0] == point[0] and x != point, points))
    on_y = list(filter(lambda x: x[1] == point[1] and x != point, points))
    print(on_x, on_y)
    print()
