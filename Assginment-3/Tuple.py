#Blank Tuple
tup = ()
print(tup)
print(type(tup))

#Create 1st Tuple
tup1 = (22.3, 38.8, 78.2)
print(tup1)

#Print any element from Tuple 1
print(tup1[1])

#Create 2nd Tuple
tup2 = (36, 72, 82, 43)
print(tup2)

#Print any element from Tuple 2
print(tup2[2])

#Nesting of Tuple
nested_tuple = (tup1, tup2)
print(nested_tuple)

#Concatinate Both Tuple
Concatinated_Tuple = tup1 + tup2
print(Concatinated_Tuple)

#indexing A Tuple
#Print Any Number Using Index

tup = (1, 3, 2, 1, 2, 3)
print(tup.index(3))

#Counting Methode
#How much time this number is present 

tup = (1, 3, 2, 1, 2, 3)
print(tup.count(3))