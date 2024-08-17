def twoSum(nums, target):
    hashMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[n] = i

nums = [2,3,14,9,4,8,28,16,6,12]
target = 12

print(twoSum(nums, target))