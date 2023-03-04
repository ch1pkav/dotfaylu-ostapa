points = set()
n = int(input())
for i in range (n):
    points.add(tuple(map(int, input().split())))
rectangles = set()

for point in points:
    on_x = set(filter(lambda x: x[0] == point[0] and x != point, points))
    on_y = set(filter(lambda x: x[1] == point[1] and x != point, points))
    for x in on_x:
        for y in on_y:
            if (x[1], y[0]) in points and (x[1], y[0]) != point and (x[0] != y[0] and x[1]!=y[1]): 
                if (point, y, x, (x[1], y[0])) not in rectangles:
                    rectangles.add((point, x, y, (x[1], y[0])))

print(rectangles)
print(len(rectangles))