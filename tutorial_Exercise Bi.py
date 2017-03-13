# Changed to "How to Think Like a Computer Scientist:
# Learning with Python 3"

# 2.12 The modulus operator 
# Write a program to ask the user to enter some secons, and we'll
# convert them to hours, minutes and seconds

total_seconds = 341324 # int(input("How many seconds? "))
min_per_hour = 3600
sec_per_minute = 60
hours = total_seconds // min_per_hour
seconds_remaining = total_seconds % min_per_hour
minutes = seconds_remaining // sec_per_minute
seconds = seconds_remaining % sec_per_minute
print(hours, minutes, seconds)

# 2.14 [2;12]z
# Exercise 1
# Take the sentence: All work and no play makes jack a dull boy
# Stor each word in a separate variable then print out the sentence
# on one line using print()
a = 'All'
b = 'work'
c = 'and'
d = 'no'
e = 'play'
f = 'makes'
g = 'Jack'
h = 'a'
j = 'dull'
k = 'boy'
l = ' '
print(a + l + b + l + c + l + d + l + e + l + f + l + g + l + h + l + j + l + k)

# Exercise 2 - 4 done in interpreter
# Exercise 5
# Assign the principal amount of $10000 to variable p assign to n
# the value 12 and assign to r the interest rate of 8%. Then have
# the program promt the user for the numver of years t that the
# money will be compounded. Print final ammount.
## experession A = P(1 + (r / n))**(nt)
P = 10000
n = 12
r = 0.08
t = int(input('How many years will it be compounded for? '))
A = P * (1 + (r / n)) ** (n * t)
print(A)

# Exercise 6 - 7 in interpreter
# Exercise 8
# Calculate the time an alarm will go off given a random int
current_time = int(input('What is the current hour? '))
am_pm = input('Is it am or pm? ')
user_hours = int(input('How many hours? '))
no_days = 24
remaining_hours = current_time % user_hours
if am_pm == 'am':
    print(str(current_time + remaining_hours) + 'am')
else:
    print(str(current_time + remaining_hours) + 'pm')
