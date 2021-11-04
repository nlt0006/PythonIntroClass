"""
Answers to last week's assignment:
"""
# schools = {'UAH': {'enrollment': 10000, 'location' : 'Huntsville, AL', 'colors' : 'Blue and white'},
#            'UAB':{'enrollment': 20000, 'location' : 'Birmingham, AL', 'colors' : 'Green'},
#            'UA':{'enrollment': 35000, 'location' : 'Tuscaloosa, AL', 'colors' : 'Crimson'}}
#
# uah_higher = (schools['UAH']['enrollment'] > schools['UAH']['enrollment'])
# print(uah_higher)
#
# schools['Auburn'] = {'enrollment': 30000, 'location' : 'Auburn, AL', 'colors' : 'Blue and Orange'}
# print(schools)
#
# print((10%3)+17)
#
# my_list = [135, 3158, 97, 23, 8931456]
#
# print(my_list[4]/my_list[2])
# print((my_list[0] + my_list[3])*my_list[1])
# print(my_list[0]**(my_list[4]/my_list[1]))




"""
In this session, we will be going over if/then statements, for, and while loops
"""


"""

If/then statements make comparisons and branch the code to excute in different ways.
However the evaluation is extremely literal. It evaluates the comparison exactly
as is written. Think of it as a petulant child who says "they're not exactly the
same, though".

Also note, that you will need a colon after every if, elif, and else line

"""

# name = 'Nate'

# if name == 'Nate': #true
#     print('Hello!')
# else:
#     print("You're not Nate...")


## this will return the else statement, because the name = 'Nate' not 'nate'
# if name == 'nate': #false
#    print('Hello!')
# else:
#    print("You're not Nate...")

# # will return true
# if name == 'nate' or name == 'Nate':
#     print('Hello!')
# else:
#     print("ERROR: This didn't work")




###################


# var_a = 3129
# var_b = 33
#
# if var_a % 2 == 0:
#     print(var_a, "is even")
# elif var_b % 2 == 0:
#     print(var_b, "is even")
# else:
#     print("Neither {}, nor {}, are even".format(var_a, var_b))


###################


# var_a = 408
# var_b = 1092
#
# test_var = 1100
#
# if test_var > var_a and test_var < var_b:
#     print("It's in the middle.")
# elif test_var > var_a and test_var > var_b:
#     print("{} is the highest value...".format(test_var))
# else:
#     print("{} is the lowest value...".format(test_var))




"""
For loops are elements of code which execute iteratively 'for' every x in y.
They continue to run until they get to the end of the specified parameters, or
until 'break' is reached. For loops can be great for any number of actions which require you to go through
a list, set, options, or actions.

The general structure of a for loop is:

for iteration in item_iterated
The 'iteration' term can be anything you want it to be, and the item_iterated is
whatever you want to iterate through.
"""

# for i in range(10):
#     print(i**2)

###################

# names_list = ['Nate', 'Eric', 'Raja', 'Jenna', 'Andrew', 'Amber']
#
# for name in names_list:
#     print("Hello {}".format(name))

###################

# for s in "Hello from the otherside":
#     print(s)

###################

# for num in range(1, 21, 3): #start at 1, go to 21 (non inclusive), every 3 numbers
#     if num%2 == 0:
#         print("{} is even".format(num))
#     elif num%19 == 0:
#         break
#     else:
#         print("{} is odd".format(num))

###################

"""
While loops are very similar to for loops, except they do not iterate. Intstead
they loop while a condition remains true. Once that condition is no longer true,
they break.

So, for example, while 1 > 0: would always run because 1 will never be less than 0.

Similarly while True: will always run. Often, programmers will use while True to
simply keep looping until some event trigger in the code breaks them out.

Just as with if, and for statments, a colon needs to be put at the end of the initial statement.
"""

# count = 0
#
# while count < 100:
#     print(count)
#     count += 1

###################

# name = ''
#
# while name != 'end':
#     name = input("What is your name? ")
#     print("Hi, {}!".format(name))

# while True:
#     name = input("What is your name? ")
#     if name == 'end':
#         break
#     else:
#         print("Hi, {}!".format(name))


# for num in range(100):
#     count = 0
#     orig_val = num
#     while num > 1:
#         if num % 2 == 0:
#             num /= 2
#         else:
#             num = (3 * num) + 1
#         count += 1
#     print("{} takes {} steps to reach 1".format(orig_val, count))


"""
Practice "assignment" for next time:

1. Create a dictionary with usernames and passwords. Then create an interaction where
users are asked for their username, then iterate through all of the keys in the dictionary
to find the username. If you can find the username, then ask them for the password. If
you cannot find the username, tell them "Username was not found". If their password
is correct give them a "Welcome!" message. If it isn't correct, ask them to try again. Only give them
3 tries at the password. If they fail three times in a row, tell them that they are now locked
out of their account.

2. Write an algorithm that finds every prime number under 100.
"""
