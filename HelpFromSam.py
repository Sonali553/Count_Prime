def Help_from_Sam(A):
  r = 1
  while(r * 2 <= A):
    r *= 2
  
  return A - r + 1
print(Help_from_Sam(5))
print(Help_from_Sam(3))
print(Help_from_Sam(1))
print(Help_from_Sam(8))
print(Help_from_Sam(4))