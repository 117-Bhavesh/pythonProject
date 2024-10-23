'''

birth_year = input('Birth year: ')
age = 2024 - birth_year
print(age)

#this program showed this error
#TypeError: unsupported operand type(s) for -: 'int' and 'str'
#it means we were trying to subtract string form int which isnt supported
#after string is executed in first line of code
#whatever the user enters will be stored as string only

'''

birth_year = input('Birth year: ')
#whenever you use a input function you always get a string
age = 2024 - int(birth_year)
#if we add int before the variable containing the string
#it will get converted to int
print(age)

#to check the data type of the variable
print(type(birth_year))
print(type(age))