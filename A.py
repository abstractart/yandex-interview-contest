J = input()
S = input()

jewels = set(J)
result = 0

for s in S:
  if s in jewels:
    result += 1

print(result)
