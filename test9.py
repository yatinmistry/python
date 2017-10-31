#!C:\Program Files (x86)\Python36-32\python.exe
#python tuple and list update
import config

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
# tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 100000000     # Valid syntax with list

print(tuple,list)