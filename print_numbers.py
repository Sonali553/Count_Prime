
def printNumber(N):
  if N == 1:
    print(1)
    return 
  printNumber(N - 1)
  print(N)
printNumber(10)