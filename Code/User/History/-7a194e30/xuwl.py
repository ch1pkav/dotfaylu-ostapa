points = []
n = int(input())
for i in range (n):
    points.append(tuple(map(int, input().split())))

for point in points:
    on_x = list(filter(lambda x: x[0] == point[0], points))
    on_y = list(filter(lambda x: x[1] == point[1], points))
    print(on_x, on_y)
    print()
    