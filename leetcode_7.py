class Solution:
    def reverse(self, x: int) -> int:
        string = str(abs(x))
        res = string[::-1]
        res = int(res)
        print(res, (-2) ** 31, (2 ** 31 -1))
        if res < ((-2) ** 31) or res > (2 ** 31 -1):
            return 0
        if x > 0:
            return res
        else:
            res = -res
            return res

    def reverse_(self, x: int):
        ans = 0
        flag = 1
        if x < 0:
            flag = -1
            x = abs(x)
        while x != 0:
            pop = x % 10
            ans = ans * 10 + pop
            if ((-2) ** 31) < ans < (2 ** 31 - 1):
                pass
            else:
                return 0
            x = x // 10
        return ans * flag


if __name__ == "__main__":
    x = -158
    test = Solution()
    print(test.reverse_(x))

