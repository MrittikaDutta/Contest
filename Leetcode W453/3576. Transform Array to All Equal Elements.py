class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def mot(target: int) -> int:
            wrong = [1 if num != target else 0 for num in nums]
            ops = 0
            n = len(wrong)
            for i in range(n-1):
                if wrong[i]:
                    wrong[i] ^= 1
                    wrong[i+1] ^= 1
                    ops += 1
            return ops if wrong[-1] == 0 else float('inf')
        return min(mot(1), mot(-1)) <= k
