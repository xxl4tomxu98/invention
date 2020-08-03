def superDigit(n,k):
  n_str = str(n)
  if len(n_str) == 1:
    return n_str
  sub_total = 0
  for char in n_str:
    sub_total += int(char)
  total = sub_total * k
  return superDigit(total, 1)


#here is a short version

def superDigit1(n,k):
  x = (n * k) % 9
  return x if x else 9


if __name__ == '__main__':
  print(superDigit(123124, 2))
  n, k = map(int, input().split())
  print(superDigit1(n,k))
