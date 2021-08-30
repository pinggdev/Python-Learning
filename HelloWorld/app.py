# How Python Code Gets Executed
# print("Kevin Sinaga")
# print("*" * 10)



#variable
# price = 10
# rating = 4.9
# name = 'Kevin'
# is_published = True
# print(price)

# name = 'Kevin'
# age = 20
# is_new = True



# Receiving Input
# name = input('What is your name? ')
# print('Hi ' +  name)

# name = input('What is your name? ')
# favorite_color = input('What is your favorite color? ')
#
# print(name + ' likes ' + favorite_color)

# birth_day = input('Birth year: ')
# print(type(birth_day))
# age = 2021 - int(birth_day)
# print(type(age))
# print(age)



#Type Conversion
# weight_lbs = input('Weight (lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)



#Strings
# course = '''
#     Testing for email...
#     This is the first email...
# '''
# course = 'Python for beginners'
# print(course[:])



#formatted strings
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + ' ]' + ' is a coder'
# msg = f'{first} [{last}] is a coder'
# print(msg)



#string methods
# course = 'Python for Beginners'
# print(course.upper())
# print(course.find('o'))
# print(course.replace('Beginners', 'Absolute Beginners'))



#arithmetic operations
# x = 10
# x += 3 # augmented assignment operator
# print(x)



#operator precedence
# x = (10 + 3) * 2 ** 2
# print(x)



#Math Functions
# import math
# print(math.ceil(2.9))



#If Statements
# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")



# Logical Operators
# has_high_income = False
# has_good_credit = True
# has_criminal_record = True
#
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")



# Comparison Operators
# temperature = 35
#
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# name = input('Masukkan nama anda: ')
#
# if len(name) < 3:
#     print("Name must be at least 3 characters.")
# elif len(name) > 50:
#     print("Name must be a maximum of 50 characters.")
# else:
#     print("Name looks good!")



# Weight Converter Program
# weight = int(input("Weight: "))
# unit = input("(L) bs or (K)g: ")
#
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")



# While Loops
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("Done")



# Building a Guessing Game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed')