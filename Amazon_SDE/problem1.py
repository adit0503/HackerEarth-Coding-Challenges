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

def solve2(N, A):

    def getDivisors(n):
        divisors = set()
        for i in range(1, int(n**0.5)+1):
            if not n%i:
                divisors.add(i)
                divisors.add(n//i)
        return divisors
    
    divisor_count = {}
    divisor_element = {}
    for a in A:
        divisors = getDivisors(a)
        for div in divisors:
            divisor_count[div] = divisor_count.get(div,0) + 1
            divisor_element[div] = divisor_element.get(div, []) + [a]

    all_divisors = list(divisor_count.keys())
    for d in all_divisors:
        if divisor_count[d] < 2:
            del divisor_count[d]
            del divisor_element[d]
            
    print(sorted(divisor_count.items(), reverse=True))
    print(sorted(divisor_element.items(), reverse=True))

solve2(3, [8, 5, 6, 25, 6, 16])