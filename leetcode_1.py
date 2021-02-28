class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            value = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == value:
                    return [i, j]

    def twoSum_(self, nums, target):
        dict1 = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums) - 1):
            value = target - nums[i]
            if value in dict1 and dict1[value] != i:
                return [i, dict1[value]]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    if Solution().twoSum(nums, target) == [0, 1]:
        print("Result is right ! ")
    if Solution().twoSum_(nums, target) == [0, 1]:
        print("Result is right ! ")

