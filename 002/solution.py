MAX = 4000000

first_number = 1
second_number = 1

sum = 0

while second_number <= MAX:
    temp = second_number
    second_number += first_number
    first_number = temp

    if second_number % 2 == 0:
        sum += second_number
print(sum)
