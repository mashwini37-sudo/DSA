def second_largest(arr):
    largest = second = -1
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num != largest and num > second:
            second = num
    return second

print(second_largest([8, 8, 2, 3, 5, 5]))  