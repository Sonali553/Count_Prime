s = "Hello"
def simpleReverse(s):
    res = ""
    n = len(s) - 1
    while(n >= 0):
        res += s[n]
        n -= 1
    return res
print(simpleReverse("Scaler"))
print(simpleReverse(s))

