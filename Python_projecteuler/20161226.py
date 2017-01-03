from time import time
start = time()

i = 125874
flag = True
while flag:
    i += 9
    if sorted(str(i)) == sorted(str(2*i)) == sorted(str(3*i)) == sorted(str(4*i)) == sorted(str(5*i)) == sorted(str(6*i)):
        flag = False
print(i)

print(time()-start)
# def multiples_have_same_digits(n):
#      digit_keys = dict.fromkeys(list(str(n)))
#      for x in range(2, 4):
#          for d in list(str(x * n)):
#              if d not in digit_keys: return False
#      return True
#
# n = 0
# while True:
#      n = n + 9                           # n must be a multiple of 9 for this to happen
#      if multiples_have_same_digits(n):
#          print(n)
#          break

print(time()-start)