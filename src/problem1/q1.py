def first_way(n):
  result = 0
  for i in range(1, n+1):
    result += i
  return result

def second_way(n):
  if n == 0:
    return 0
  else:
    return n + second_way(n-1)

def third_way(n):
  arr = []
  for i in range(1, n+1):
    arr.append(i)
  return sum(arr)

N = 10

print(first_way(N))
print(second_way(N))
print(third_way(N))