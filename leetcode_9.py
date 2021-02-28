class Solution:
    def isPalindrome(self, x: int) -> int:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        resvertedNum = 0
        while x > resvertedNum:
            resvertedNum = resvertedNum * 10 + x % 10
            x = x // 10
        return x == resvertedNum or x == resvertedNum // 10


if __name__ == "__main__":
    x = 12321
    test = Solution()
    print(test.isPalindrome(x))

