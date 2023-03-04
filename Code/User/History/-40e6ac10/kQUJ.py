n, m = tuple(map(int, input().split()))
pairs = []
for i in range(m):
    pairs.append(tuple(map(lambda x: int(x)-1, input().split())))

lexo = []
printnext = True

# nums = [False for i in range(m)]
pairs = sorted(pairs)
for pair in pairs:
    if pair[0] not in lexo and pair[1] not in lexo:
        lexo.append(pair[0])
        lexo.append(pair[1])
    elif pair[1] in lexo and pair[0] not in lexo:
        print(-1)
        printnext = False
        break
    elif pair[0] in lexo and pair[1] not in lexo:
        lexo.append(pair[1])
    else:
        if lexo.index(pair[0])>lexo.index(pair[1]):
            print(-1)
            printnext = False

lexo = list(map(lambda x: x+1, lexo))
if printnext:
    print(*lexo)

