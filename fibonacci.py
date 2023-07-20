"0 0 1 1 2 3 5 8 13"
def fibonacci(N):
  if N == 0:
    return 0
  if N == 1:
    return 1
  return fibonacci(N - 1) + fibonacci(N - 2)
for i in range(5):
  print(fibonacci(i))

