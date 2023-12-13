def SieveOfEratosthenes(num):
  primes = []
  prime = [True for i in range(num+1)]
  p = 2
  while(p*p <= num):
    if (prime[p] == True):
      for i in range(p*p,num+1,p):
        prime[i] = False
    p += 1

  for p in range(2,num+1):
    if prime[p]:
      primes.append(p)
  return primes

def funct(num):
  if(num < 5):
    return(f"{num} is less than 5")
  elif(num < 50):
    return(f"{num} is between 5 and 5")
  else:
    return(f"{num} is 50 or higher")

def MinMaxSum2(*args):
  nums = []
  for number in args:
    nums.append(number)
  lowest = min(nums)
  highest = max(nums)
  added = sum(nums)
  result = (lowest, highest, added)
  return result
