def longest_PldSubstring(s):
    n = len(s)
    maxlength = 0
    for i in range(0, n):
        r = i
        l = n - 1
        
        while(l >= 0 and r < n):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
        maxlength = max(maxlength, (r - l + 1))
    return maxlength
print(longest_PldSubstring("aba"))
print(longest_PldSubstring("abba"))
        
        
