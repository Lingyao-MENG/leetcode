class Solution:
    def _valid(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        maxlong = 1
        res = s[0]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if j - i + 1 > maxlong and self._valid(s, i, j):
                    maxlong = j - i + 1
                    res = s[i: j+1]
        return res

    def longestPalindrome_(self, s):
        size = len(s)
        if size < 2:
            return s
        dp = [[False]*size for _ in range(size)]
        for i in range(size):
            dp[i][i] = True
        maxlen = 1
        start = 0

        for j in range(size):
            for i in range(j):

                if s[i] == s[j]:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                print(i, j, maxlen, s[i], s[j], j-i+1, dp[i][j])
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > maxlen:
                        maxlen = cur_len
                        start = i

        return s[start: start + maxlen]

    def longestPalindrome__(self, s):
        size = len(s)
        if size < 2:
            return s
        max_len = 1
        res = s[0]
        for i in range(size):
            string_odd, len_odd = self._s_valid(s, size, i, i)
            string_even, len_even = self._s_valid(s, size, i, i+1)
            if len_odd < len_even:
                cur_string = string_even
            else:
                cur_string = string_odd
            if len(cur_string) > max_len:
                max_len = len(cur_string)
                res = cur_string
        return res

    def _s_valid(self, s, size, left, right):
        i = left
        j = right
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i:j], j-i+1


if __name__ == "__main__":
    string = "cccc"
    test = Solution()
    print(test.longestPalindrome__(string))


