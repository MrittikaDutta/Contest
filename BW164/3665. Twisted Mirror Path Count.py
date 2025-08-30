class Solution:
    def uniquePaths(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0])
        mod=10**9+7
        mem={}
        def s(i,j,d):
            
            k=(i,j,d)
            if k in mem: 
                return mem[k]
            r,c=i,j
            if d==0: 
                c+=1
            else: 
                r+=1
            ed=d
            while True:
                if r<0 or r>=m or c<0 or c>=n:
                    mem[k]=None
                    return None
                if g[r][c]==0:
                    mem[k]=(r,c)
                    return (r,c)
                if ed==0:
                    r+=1
                    ed=1
                else:
                    c+=1
                    ed=0
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                v=dp[i][j]
                if not v: 
                    continue
                for d in (0,1):
                    rj=s(i,j,d)

                    
                    if rj is None: 
                        continue
                    x,y=rj
                    dp[x][y]=(dp[x][y]+v)%mod
        return dp[m-1][n-1]%mod
