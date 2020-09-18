def helper(s, l, r, n):
    if l == r and r == n:
        print(s)
    if l < n:
        helper("{}(".format(s), l + 1, r, n)

    if r < n and r < l:
        helper("{})".format(s), l, r + 1, n)

helper("", 0, 0, int(input()))
