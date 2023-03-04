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
count = 0
while cur_x <= x and cur_y<=y:
    if menus_bur[left] != menus_dog[right]:
        if sum(menus_bur[left]) < sum(menus_dog[right]):
            cur_x+=menus_dog[right][0]
            cur_y+=menus_dog[right][1]
            count+=1
            right+=1
            if cur_x <= x and cur_y<=y:
                cur_x+=menus_bur[left][0]
                cur_y+=menus_bur[left][1]
                count+=1
                left+=1
        else:
            cur_x+=menus_bur[left][0]
            cur_y+=menus_bur[left][1]
            count+=1
            left+=1
            if cur_x <= x and cur_y<=y:
                cur_x+=menus_dog[left][0]
                cur_y+=menus_dog[left][1]
                count+=1
                right+=1
    else:
        cur_x+=menus_bur[left][0]
        cur_y+=menus_bur[left][1]
        count+=1
        left+=1
        right+=1



if cur_x< x and cur_y < y:
    print(-1)
else:
    print(count)