class Solution:
    def minArray(self, numbers) -> int:
        left, right = 0, len(numbers)-1
        while left < right:
            mid = left + (right - left) // 2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1
            print(left, mid, right)
        return numbers[left]

        return min(numbers)


if __name__ == "__main__":
    numbers = [3, 1, 3]
    test = Solution()
    print(test.minArray(numbers))
