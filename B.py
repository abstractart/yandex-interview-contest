def main():
    n = int(input())

    result = 0
    curr = 0
    for i in range(n):
        val = int(input())
        if val == 1:
            curr += 1
        if val == 0:
            result = max(result, curr)
            curr = 0

    return max(result, curr)

print(main())
