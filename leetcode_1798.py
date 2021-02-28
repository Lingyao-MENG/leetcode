class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        grid = [[0]*n for _ in range(m)]
        board = [[False]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = i//100 + i//10 + i%10 + j//100 + j//10 + j%10
        for one in grid:
            print(one)

        def dfs(i, j):
            value = grid[i][j]
            if not 0 <= i < m or not 0 <= j < n or value > k:
                return False
            if value <= k and (board[i][j+1] == True or board[i+1][j] == True):
                board[i+1][j+1] = True
                return True
            else:
                return False

        res = 1
        board[1][1] = True
        for x in range(m):
            for y in range(n):
                print(x,y)
                if dfs(x, y):
                    res += 1
        return res


if __name__ == "__main__":
    m, n, k = 3, 2, 17
    test = Solution()
    print(test.movingCount(m, n, k))

