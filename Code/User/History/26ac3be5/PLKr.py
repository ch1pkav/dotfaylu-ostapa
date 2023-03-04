start = 0
sum = 0
n, left, right = tuple(map(int, input().split()))
moleculas = list(map(int, input().split()))
moleculas = sorted([(val, ind) for ind, val in enumerate(moleculas)], key = lambda x: x[0])
def func(moleculas, start, sum):
    for i in range(len(moleculas)):
        sum += moleculas[i][0]
        if sum > right:
            sum -= moleculas[start][0]
            start+=1
        if sum <= right and sum >= left:
            print(i-start+1)
            for j in range(start, i):
                print(moleculas[j][1], end = " ")
            print()
            return
    print(0)
    return
func(moleculas, start, sum)

