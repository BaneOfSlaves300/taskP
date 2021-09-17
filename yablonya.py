n = int(input())

li = list(map(int, input().split()))


for i in range(len(li)):
    li[i] -= 1

A = [0 for i in range(n)]

A[0] = 1

for i in range(n - 1):
    A[i + 1] = A[li[i]] + 1

A.sort()

ans = 0
cur = 1
len = 0

for i in A:
    if i == cur:
        len += 1
    else:
        ans += len % 2
        len = 1
        cur = i
ans += len % 2
print(ans)
