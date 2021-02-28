
class Solution():

    # 求区间的和可以用 preSum
    def findMaxAverage(self, nums, k):
        N = len(nums)
        if N > 0:
            preSum = [0] * (N + 1)
            for i in range(N):
                preSum[i + 1] = preSum[i] + nums[i]
            largest = float("-inf")
            for i in range(k - 1, N):
                largest = max(preSum[i + 1] - preSum[i + 1 - k], largest)
            return largest / k
        else:
            return 0

    def findMaxAverage_(self, nums, k):
        N = len(nums)
        sum = 0
        if N > 0:
            largest = float("-inf")
            for i in range(N):
                sum += nums[i]
                if i >= k:
                    sum -= nums[i-k]
                if i >= k-1:
                    largest = max(sum, largest)
            return largest/float(k)
        else:
            return 0


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(Solution().findMaxAverage(nums=nums, k=k))
    print(Solution().findMaxAverage_(nums=nums, k=k))