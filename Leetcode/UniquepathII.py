class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
    
        m = len(obstacleGrid)  # ✅ Correctly indented
        # ... other code
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        # Start position
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # Fill first column
        for i in range(1, m):
            dp[i][0] = 1 if dp[i-1][0] == 1 and obstacleGrid[i][0] == 0 else 0

        # Fill first row
        for j in range(1, n):
            dp[0][j] = 1 if dp[0][j-1] == 1 and obstacleGrid[0][j] == 0 else 0

        # Fill rest of grid
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
