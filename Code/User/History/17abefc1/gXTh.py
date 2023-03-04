import bisect
n, m = tuple(map(int, input().split()))
vector_a = sorted(list(map(int, input().split())))
vector_b = sorted(list(map(int, input().split())))

left = 0
right = 0

min_sum = float("inf")
# for a in vector_a:
#     for b in vector_b:
#         min_sum = min(min_sum, abs(a-b))

for num in vector_a:
    ind = bisect.bisect_left(vector_b, num)
    if ind != 0:
        min_sum = min(min_sum, abs(num - vector_b[ind-1]))
    min_sum = min(min_sum, abs(num - vector_b[ind]))

print(min_sum)
