lst = list(map(int, input().split()))
def element_Removal(A):
  A.sort(reverse = True)
  res = 0
  for i in range(0, len(A)):
    res += ((i + 1) * A[i])
  return res
print(element_Removal([2, 1]))
print(element_Removal([5]))
print(element_Removal(lst))