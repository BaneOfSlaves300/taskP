n, k = map(int, input().split())
li = [list(input()) for i in range(n)]
I = [[0 for i in range(n)] for j in range (n)]
I[0][0] = 1
if (li[0][0] == 'a'):
    I[0][0] = 0

if k > 0 :
    li[0][0] ='a'

for i in range(1, n):
    if (li[0][i] == 'a'):
        I[0][i] = I[0][i - 1]
    else :
        I[0][i] = I[0][i - 1] + 1
    if (I[0][i] <= k) :
        li[0][i] = 'a'

for i in range(1, n):
    if (li[i][0] == 'a'):
        I[i][0] = I[i - 1][0]
    else :
        I[i][0] = I[i - 1][0] + 1
    if (I[i][0] <= k) :
        li[i][0] = 'a'

for i in range(1, n):
    for j in range (1, n):
        a = min(I[i][j - 1], I[i - 1][j]) + 1
        if li[i][j] == 'a':
            a -= 1
        I[i][j] = a
        if I[i][j] <= k:
            li[i][j] = 'a'

current = set([0])

s = str(li[0][0])
next = set()

while len(s) < 2 * n - 1:
    var = 'zz'
    for i in current:
        x = i % n
        y = i // n
        x1 = x + 1
        y1 = y + 1
        if x1 < n and li[x1][y] == var:
            next.add(y * n + x1)
        if x1 < n and (var == 'zz' or li[x1][y] < var):
            next.clear()
            next.add(y * n + x1)
            var = li[x1][y]
        if y1 < n and li[x][y1] == var:
            next.add(y1 * n + x)
        if y1 < n and (var == 'zz' or li[x][y1] < var):
            next.clear()
            next.add(y1 * n + x)
            var = li[x][y1]
    if var != 'zz':
        s += var
    current.clear()
    for i in next:
        current.add(i)
ans = list(s)
print(''.join(ans))
