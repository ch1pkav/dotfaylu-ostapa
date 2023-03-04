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
            if (y[0], x[1]) in points and (y[0], x[1]) != point:
                if (point, y, x, (y[0], x[1])) not in rectangles:
                    rectangles.add((point, x, y, (y[0], x[1])))
            

# print(rectangles)
print(len(rectangles)/4)