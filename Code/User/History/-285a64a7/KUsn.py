n = int(input())
x, y = tuple(map(int, input().split()))
menus = []
for i in range (n):
    menus.append(tuple(map(int, input().split())))

cur_x = 0
cur_y = 0
valid = False
menus_bur = sorted(menus, key = lambda x: x[0], reverse=True)
menus_dog = sorted(menus, key = lambda x: x[1], reverse=True)
# print(menus)
left = right = 0
while cur_x <= x and cur_y<=y:
    if menus_bur[left] != menus_dog[right]:
        cur_x+=menus_dog[right][0]
        cur_x+=menus_bur[left][0]
        cur_y+=menus_dog[right][1]
        cur_y+=menus_bur[left][1]
    else:
        cur_x+=menus_bur[left][0]
        cur_y+=menus_bur[left][1]
    left+=1
    right+=1


if not valid:
    print(-1)