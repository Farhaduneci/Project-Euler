sum = 0

for integer in range(1, 1000):
    if integer % 3 == 0 or integer % 5 == 0:
        sum += integer
print(sum)
