pattern = input().strip()
genome = input().strip()

positions = []

for i in range(len(genome) - len(pattern) + 1):
    if genome[i:i + len(pattern)] == pattern:
        positions.append(str(i))

print(" ".join(positions))
