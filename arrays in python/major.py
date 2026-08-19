arr = [2, 2, 1, 1, 1, 2, 2]

candidate = 0
count = 0

for num in arr:
    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

print(candidate)