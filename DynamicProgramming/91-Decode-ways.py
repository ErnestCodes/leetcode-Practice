# can cur char be decoded in one or two ways? Recursion -> cache -> iterative dp solution, 
# a lot of edge cases to determine, 52, 31, 29, 10, 20 only decoded one way, 11, 26 decoded two ways
class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = { len(s) : 1 }
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or 
                s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)

        # Dynamic Programming
        dp = { len(s) : 1 }
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if (i + 1 < len(s) and (s[i] == "1" or 
                 s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        return dp[0]
