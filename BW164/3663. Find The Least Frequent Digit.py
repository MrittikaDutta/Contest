class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s = str(n)
        d = {i: s.count(i) for i in s}
        
        m = min(d.values())
        r = [int(k) for k, v in d.items() if v == m]
        return min(r)
