def house_Robber(nums):
    c = 0
    for i in range(0, len(nums), 2):
        c += nums[i]
    return c
print(house_Robber([1, 2, 3, 1]))
print(house_Robber([2, 7, 9, 3, 1]))