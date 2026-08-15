numbers = [10, 20, 10, 30, 10]

count = numbers.count(10)

while count > 1:
    numbers.remove(10)
    count -= 1

print(numbers)
