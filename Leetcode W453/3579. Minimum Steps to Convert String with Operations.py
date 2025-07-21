class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        def cost(a: str, b: str) -> int:
            m = len(a)
            mm = 0
            
            counts = {}
            for i in range(m):
                if a[i] != b[i]:
                    mm += 1
                    key = (a[i], b[i])
                    counts[key] = counts.get(key, 0) + 1
            swaps = 0
            for (x, y), cxy in counts.items():
                yx = (y, x)
                if yx in counts:
                    swaps += min(cxy, counts[yx])
            swaps //= 2
            return mm - swaps

        dp = [10**9] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i):
                a = word1[j:i]
                b = word2[j:i]
                no_rev = cost(a, b)
                rev = 1 + cost(a[::-1], b)
                dp[i] = min(dp[i], dp[j] + min(no_rev, rev))
        return dp[n]
