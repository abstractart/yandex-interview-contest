n = int(input())
prev = None

for i in range(n):
    val = input()
    if val != prev:
        print(val)
    prev = val
