def hamming_distance(s1, s2):
  count = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      count += 1
  return count

pattern = input().strip()
text = input().strip()
d=int(input())

positions = []
k=len(pattern)

for i in range(len(text) - k + 1):
  substring = text[i:i +k]

  if hamming_distance(pattern, substring) <= d:
    positions.append(str(i))
print(" ".join(positions))
