def faktorer(num):
  factors = []
  for whole_number in range(1, num + 1):
    if num % whole_number == 0:
      factors.append(whole_number)
      #factors.append(-whole_number)
  print(factors)
  return factors