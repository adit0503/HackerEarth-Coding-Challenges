def solve(N,S):

    def getSubstringCount(k):
        ans = 0

        j, temp = 0, {}
        for i in range(N-k+1):
            while(j<N and len(temp)<k):
                temp[S[j]] = temp.get(S[j], 0) + 1
                j += 1
            if len(temp) == k:
                ans += N-j+1
                
            if temp[S[i]] == 1:
                del temp[S[i]]
            else:
                temp[S[i]] = temp.get(S[i]) - 1
        return ans
    
    result = []
    for i in range(1,27):
        result.append(getSubstringCount(i))
    return result
