from os import linesep

quote_1 = 'The future belongs to those who believe in the beauty of their dreams.'
quote_2 = "The future belongs to those who believe in the beauty of their dreams."
quote_3 = '''The future belongs to those 
who believe in the beauty of their dreams.'''
#three ways to print a string use whichever symbol is free to use
#the triple apostrophe can be used to print multiline strings

print(quote_1)
print(quote_2)
print(quote_3)

print(quote_2[0])
#to return a letter of certain index we need to type it within []
#index of the first character in python is 0
#0 is the index
#-1 is the index of the first character from the end

print(quote_2[4:10])
#to return letters between 0 and 3 index range
#index range can be established by using : between two indexes
#the white spaces do not have any index to them

#there is a default value to both start index and end index
#so when index isnt assigned, python assumes the default indexes
print(quote_1[:15])
print(quote_1[0:])
print(quote_2[4:])
print(quote_2[:10])
print(quote_2[:]) #this will print all the strings

thought = quote_2[:]
print(thought)
name = 'Ness117'
print(name[1:-1])