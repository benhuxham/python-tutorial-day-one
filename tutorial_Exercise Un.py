# https://automatetheboringstuff.com/chapter1/
# Tutorial attempt.

# Where possible I'll work with dozenal numbers.
# As most calculations will assume Base Ten, I'll try indicate where the
# dozenal numbers are used. Unfortunately they shall all be strings as I do not
# [yet] know how to create my own number system that is a drop in replacment
# for pervasive Base Ten

# Exercise Un  
# This program says hello and ask for my name.

print('Hello World')
print('What is your name?') # ask for their name
my_name = input()
print('It is good to meet your, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?') # ask for their age
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
