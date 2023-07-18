n = int(input())
def countOf_1Bits(n):
    c = 0
    while(n > 0):
      r = n % 2
      if r == 1:
         c += 1
      n = n // 2
    return c
print(countOf_1Bits(11))
print(countOf_1Bits(6))
print(countOf_1Bits(n))
