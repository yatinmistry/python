import sys;
list = [1,2,3,4]
it = iter(list) # this builds an iterator object
# print (next(it)) #prints next available element in iterator
# # Iterator object can be traversed using regular for statement
# print(next(it))


while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit()