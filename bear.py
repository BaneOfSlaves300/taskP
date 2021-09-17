n, k = map(int, input().split())
a, b, c, d = map(int, input().split())
boolshit = [a, b, c, d]

if (n < 5 or k < n + 1):
    print(-1)
else:
    ans = []
    for i in range(1, n + 1):
        if (i not in boolshit):
            ans.append(i)
    print(a, c, *ans, d, b)
    print(c, a, *ans, b, d)
    