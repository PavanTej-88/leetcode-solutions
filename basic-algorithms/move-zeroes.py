def move_zeroes(nums):
    position = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[position], nums[i] = nums[i], nums[position]
            position += 1


# Typical test case
nums = [0, 1, 0, 3, 12]

move_zeroes(nums)
print("Typical test case:", nums)


# Edge case
nums = [0, 0, 0]

move_zeroes(nums)
print("Edge case:", nums)