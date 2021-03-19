def solve(N, A):

    def gcd(a,b):
        if b==0:
            return a 
        return gcd(b,a%b)

    GCD = {}
    for i in range(2*N):
        for j in range(i+1,2*N):
            g = gcd(A[i], A[j])
            GCD[g] = GCD.get(g, []) + [(A[i],A[j])]

    ans, n = 0, N
    visited = set()
    for k in sorted(GCD.keys(), reverse=True):
        for x,y in GCD[k]:
            if x not in visited and y not in visited:
                visited.add(x)
                visited.add(y)
                ans += k*n 
                n = max(n-1,0)
    return ans