# Solution 1: Using sort O(n * log (n)) - Time
print(int(sorted(input()) == sorted(input())))

# Solution 2: Using Counter
from collections import Counter
print(int(Counter(input()) == Counter(input())))
