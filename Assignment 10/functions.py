'''holds both functions num and num2'''

def num(num_one, num_two=''):
  '''Takes the inputted numbers, and adds them together. If the second number is not given, it is replaced with pi.'''
  if num_two:
    num_two = num_two
  else:
    num_two = 3.14159
  result = num_one + num_two
  return result, [num_one, num_two]

def num2(verbose, num_one, num_two=''):
  '''Adds the two numbers given when calling the function. A True or False must be placed first for if the result
  printed will have the inputted numbers as well. If a second number is not chosen, pi will replace it.'''
  if num_two:
    num_two = num_two
  else:
    num_two = 3.14159
  result = num_one + num_two
  if(verbose == True):
    return result, [num_one, num_two]
  else:
    return result

if __name__ == '__main__':
    print(num2(False, 5, 3))
    print(num(1, 8))
    print(num2(True, 5, 0))
    print(num(0))