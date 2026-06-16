def hamming_distance(s1,s2):
  count = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      count += 1
  return count
def neighbors(pattern, d):
  if d==0:
    return {pattern}

  if len(pattern) == 1:
    return {"A", "C", "G", "T"}
  result = set()
  suffix_neighbors = neighbors(pattern[1:],d)

  for text in suffix_neighbors:
    if hamming_distance(pattern[1:], text) < d:
      for nucleotide in "ACGT":
        result.add(nucleotide + text)
    else:
      result.add(pattern[0] + text)
  return result

text = input().strip()
k, d = map(int, input().split())

freq = {}

for i in range(len(text)-k+1):
  pattern = text[i:i +k]

  for neighbor in neighbors(pattern, d):
    if neighbor in freq:
      freq[neighbor] += 1
    else:
      freq[neighbor] = 1

max_count = max(freq.values())

answer=[]

for pattern in freq:
  if freq[pattern] == max_count:
    answer.append(pattern)

print(*answer)
