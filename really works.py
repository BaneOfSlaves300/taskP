n, k = map(int, input().split())
li = [list(input()) for j in range(n)]

for i in range(1, n):
    li[0][i] = li[0][i - 1] + li[0][i]
for i in range(1, n):
    li[i][0] = li[i - 1][0] + li[i][0]

for i in range(1, n):
    for j in range(1, n):
        li[i][j] = min(li[i - 1][j], li[i][j - 1]) + li[i][j]
        li[i - 1][j] = ''

s = list(li[n - 1][n - 1])

for i in range(2 * n - 1):
    if s[i] != 'a' and k > 0:
        s[i] = 'a'
        k -= 1
print(''.join(s))