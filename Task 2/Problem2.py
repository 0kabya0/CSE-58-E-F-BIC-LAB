string = input()
k = int(input())

patterns = []

for i in range(len(string)-k+1):
  patterns.append(string[i:i+k])

max_count = 0
for pattern in patterns:
  count = patterns.count(pattern)
  if count > max_count:
    max_count = count
printed = []

for pattern in patterns:
  if patterns.count(pattern) == max_count and pattern not in printed:
    print(pattern, end=" ")
    printed.append(pattern)
