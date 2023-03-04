n, m = tuple(map(int, input().split()))
vector_a = sorted(list(map(int, input().split())))
vector_b = sorted(list(map(int, input().split())))

min_sum = float("inf")
a_p = b_p = 0
while a_p != n and b_p != m:
    min_sum = min(abs(vector_a[a_p] - vector_b[b_p]), min_sum)
    if a_p != n:
        a_p += 1
    if b_p != m:
        b_p += 1

print(min_sum)
