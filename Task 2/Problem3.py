pattern = input()

reverse_pattern = pattern[::-1]

result= ""

for ch in reverse_pattern:
  if ch == "A":
    result+="T"
  elif ch == "T":
    result+="A"
  elif ch == "C":
    result+="G"
  elif ch == "G":
    result+="C"

print(result)
