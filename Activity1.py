#Create a Tuple With Different Data Types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)


#Create tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)


tuplex = tuplex +(9,)
print(tuplex)

#Counts The Number of Occurrences of an Element in a Tuple
tuple = (50, 10, 60, 70, 50)
print(tuple.count(50))


#Create a Tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#Used tuple[start:stop] to slice the tuple
_slice = tuplex[3:5]
print(_slice)

_slice = tuplex[:6]
print(_slice)