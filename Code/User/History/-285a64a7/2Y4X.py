n = int(input())
x, y = tuple(map(int, input().split()))
menus = []
for i in range (n):
    menus.append(tuple(map(int, input().split())))

cur_x = 0
cur_y = 0
valid = False

menus = sorted(menus, key = lambda x: x[0] + x[1])
for ind, menu in enumerate(menus):
    cur_x+= menu[0]
    cur_y+= menu[1]
    if cur_x>= x and cur_y>=y:
        print(ind+1)
        valid = True
        break

if not valid:
    print(-1)