import collections
from collections import Counter
class Solution:
    def score(self, cards: List[str], x: str) -> int:
        
        def ip(counter: Counter, add_x: int) -> int:
            total = sum(counter.values()) + add_x
            if total < 2:
                return 0
            max_count = max(list(counter.values()) + ([add_x] if add_x > 0 else [0]))
            return min(total // 2, total - max_count)
    
        
        L = Counter()
        R = Counter()
        c_xx = 0       

        for s in cards:
            if s[0] == x and s[1] == x:
                c_xx += 1
            elif s[0] == x:
                L[s[1]] += 1
            elif s[1] == x:
                R[s[0]] += 1

        best1 = 0
        for t in range(c_xx + 1):
            p_L = ip(L, t)
            p_R = ip(R, c_xx - t)
            best1 = max(best1, p_L + p_R)

        return best1
