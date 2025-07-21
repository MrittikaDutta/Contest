class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7

        
        n = len(complexity)
        m = min(complexity)
        if complexity[0] != m:
            return 0
        if complexity.count(m) > 1:
            return 0
        
        ans = 1
        for x in range(2, n):
            ans = ans * x % MOD
        return ans
