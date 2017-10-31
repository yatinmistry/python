for var in list(range(5)):
	print(var)


for letter in 'Python':     # traversal of a string sequence
   print ('Current Letter :', letter)

print()

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)


print("No of fruits  :: ",len(fruits))



print("\nGet fruits by index of list :: ")
for i in range(len(fruits)):
	print(fruits[i])




print("\nfor else ")


numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list does not contain even number')	