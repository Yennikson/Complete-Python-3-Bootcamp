# Basic Math
# float is decimals
# variables

a = 2
b = 5
c = 6
d = a**b+c


print(d)


e = (3, "de", 4)

print(type(e))

# strings
# strings are ordered, and thus can be indexed/sliced, they are also immutable

print(f"this string makes a lot of sense,\ndoesn't it?")

# indexing
# starting from 0, indexing gets yar letter

# slicing
# gives you a subset of the string, use brackets
# use : for start, stop and step; Leave something open

x = "Hello World"
print(x[:7:2])

x = x.split() #splits string based on arguments, basic is ' '
print(x)

# Formatting
# using .format

a = 'ToM,'
b = 'Jen wants a cookie'
c = ', bring her'
d = 4

print('What a day, {} {} {} {}'.format(a,b,c,d)) #variables can also be assinged inside .format()

# Lists are ordered, and thus can be indexed/sliced

list = [1,2,3,4,5,'woot']
list[3] = 6
print(f"{list[1]}")
print(f"{list.pop(3)}")

# Dictionaries
# Are unordered maps of value:key pairs
# associations made using 'thingy':'thongy'

dictionary = {'d1':'test', 'd2':['what','the','whack'], 'd3':34}
print(f"{dictionary}")
print(f"{dictionary['d2'][2]}") #you can search dicts using the key and\
# further from what's needed then

# Tuples
# Are lists that are immutable

tuple = ('a', 's', 's')
print(f"{tuple.count('s')}")

# Sets
# Unorder unique items only

sets = set(tuple)
print(f"{sets}")