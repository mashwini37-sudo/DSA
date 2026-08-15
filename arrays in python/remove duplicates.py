def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1 
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k, nums[:k]

nums = [1, 1, 2, 2, 2, 3, 4, 4]
k, result = remove_duplicates(nums)
print(k, result)