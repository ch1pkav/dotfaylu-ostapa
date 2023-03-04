points = set()
n = int(input())
for i in range (n):
    points.add(tuple(map(int, input().split())))
rectangles = set()
isrectangle = False
for point in points:
    isrectangle = False
    on_x = set(filter(lambda x: x[0] == point[0] and x != point, points))
    on_y = set(filter(lambda x: x[1] == point[1] and x != point, points))
    for x in on_x:
        for y in on_y:
            if (y[1], x[0]) in points and (y[1], x[0]) != point:
                if (point, y, x, (x[0], y[1])) not in rectangles:
                    rectangles.add((point, x, y, (x[0], y[1])))
            

print(rectangles)
print(len(rectangles))