def move_zeros_to_end(nums):
    zero_count = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
        else:
            zero_count += 1
    for i in range(zero_count):
        nums[count] = 0
        count += 1
    return nums


print(move_zeros_to_end([0, 1, 1, 2, 3, 0, 2]))
