numbers = input().split()
for i in range(len(numbers)):
  numbers[i]=int(numbers[i])
unique = []
for num in numbers:
  if num not in unique:
    unique.append(num)
if len(unique)<2:
  print(-1)

else:
  unique.sort()
  print(unique[-2])
