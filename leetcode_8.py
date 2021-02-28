class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        temp = 0
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        flag = 1
        for x in range(len(s)):
            if s[x] == " " or (not ans and s[x] == 0):
                continue
            if s[x] == "-":
                flag = -1
                continue
            elif s[x] == "+":
                flag = 1
                continue
            if (s[x] < '0' or s[x] > "9") and not ans:
                return 0
            if s[x] in nums:
                i = int(s[x])
                print("x: ", x, "i :", i, "ans: ", ans, "temp: ", temp)
                temp = ans * 10 + i
                if ((-2) ** 31) < temp < (2**31 - 1):
                    ans = temp
                    continue
                else:
                    return max(min(ans * flag, (2**31 - 1))((-2) ** 31))
        return ans * flag


if __name__ == "__main__":
    s = "words and 987"
    test = Solution()
    print(test.myAtoi(s))

