n, m = tuple(map(int, input().split()))
pairs = []
for i in range(m):
    pairs.append(tuple(map(lambda x: int(x)-1, input().split())))

lexo = []

nums = [False for i in range(n)]
pairs = sorted(pairs)
for pair in pairs:
    if not nums[pair[0]] and not nums[pair[1]]:
        nums[pair[0]] = True
        nums[pair[1]] = True
        lexo.append(pair[0])
        lexo.append(pair[1])

printnext = True
lexo = list(map(lambda x: x+1, lexo))
for num in nums:
    if not num:
        print(-1)
        printnext = False
if printnext:
    print(*lexo)

