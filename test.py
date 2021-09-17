n, k =  map(int, input().split())
li = [input() for i in range(n)]
current = set([0])

s = str(li[0][0])
next = set()

while len(s) < 2 * n - 1 :
    var = 'zz'
    for i in current:
        x = i % n
        y = i // n
        x1 = x + 1
        y1 = y + 1
        if x1 < n and li[x1][y] == var :
            next.add(y * n + x1)
        if x1 < n and (var == 'zz' or li[x1][y] < var) :
            next.clear()
            next.add(y * n + x1)
            var = li[x1][y]
        if y1 < n and li[x][y1] == var:
            next.add(y1 * n + x)
        if y1 < n and (var == 'zz' or li[x][y1] < var) :
            next.clear()
            next.add(y1 * n + x)
            var = li[x][y1]
    if var != 'zz':
        s += var
    current.clear()
    for i in next:
        current.add(i)
ans = list(s)
for i in range(n):
    if ans[i] != 'a' and k > 0:
        ans[i] = 'a'
        k -= 1
print(''.join(ans))

