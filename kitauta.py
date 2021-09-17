n, m = map(int, input().split())
M = [[[] for j in range(n)] for i in range(n)]
li = [[] for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    if b - 1 not in li[a - 1]:
        li[a - 1].append(b - 1)
    if a - 1 not in li[b - 1]:
        li[b - 1].append(a - 1)
    M[a - 1][b - 1].append(c)
    M[b - 1][a - 1].append(c)

q = int(input())
for w in range(q):
    a, b = map(int, input().split())
    num = 0
    a -= 1
    b -= 1
    colors = []
    for i in M[a]:
        for j in i:
            if j not in colors:
                colors.append(j)

    for i in colors:
        stack = [a]
        visited = [False for i in range(n)]
        visited[a] = True
        able = False
        while len(stack) > 0 and not able:
            el = stack.pop()
            ways = li[el]
            for j in ways:
                if i in M[el][j] and not visited[j]:
                    stack.append(j)
                    visited[j] = True
                    if j == b:
                        num += 1
                        able = True
                        stack = []
    print(num)
