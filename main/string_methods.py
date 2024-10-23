quote = 'The future belongs to those who believe in the beauty of their dreams.'
print(len(quote))
#to calculate the number of characters in this string we use print(len())
#len is a general purpose function in python (it is a built-in fn)
#len is not limited to just counting number of characters in a string
#eg- it can be used in list to count number of items


#method: when a function is specific to or belong to some kind of object we call it method in oop
#method can be triggered by using . after the object
print(quote.upper())
#this method doesn't modify our original string
#it creates a new string and returns it
#so we can still print the og string
print(quote)


print(quote.find('b'))
#to return the index of the first occurrence of that character
#find method is case-sensitive
#if the string to be searched doesn't exist the program will return -1

print(quote.find('future'))

line = 'So many books, so little time.'
print(line.replace('books', 'things')) #case-sensitive
#to replace an existing string with a new one
print(line.replace('b', 'l'))


print('future' in quote) #this returns a boolean value
print('Future' in quote)
#in function returns a boolean value
