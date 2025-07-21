from collections import deque

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        maxd = deque()
        mind = deque()
        L = [0] * n
        l = 0
        for i in range(n):
            while maxd and nums[maxd[-1]] < nums[i]:
                maxd.pop()
            maxd.append(i)
            while mind and nums[mind[-1]] > nums[i]:
                mind.pop()
            mind.append(i)
            while nums[maxd[0]] - nums[mind[0]] > k:
                if maxd[0] == l:
                    maxd.popleft()
                if mind[0] == l:
                    mind.popleft()
                l += 1
            L[i] = l
        
        dp = [0]*n
        prefix = [0]*n  
        for i in range(n):
            if L[i] == 0:
                dp[i] = 1 + (prefix[i-1] if i-1 >= 0 else 0)
            else:
                dp[i] = (prefix[i-1] - (prefix[L[i]-2] if L[i]>=2 else 0)) % MOD
            prefix[i] = (dp[i] + (prefix[i-1] if i-1>=0 else 0)) % MOD
        
        return dp[n-1]
