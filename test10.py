#python dictionary
dict = {}
dict['one'] = "This is one value"
dict[2]     = "This is two value"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values


# Binary representation of integer value
print(bin(10))