'''
Program to add sum of 1 to 50 odd numbers
'''

sum_of_odd = 0

for i in range(1,50,2):
    sum_of_odd += i
print("Sum of odd number from 1 to 50 is: ", sum_of_odd)    


'''
Program to add sum of 1 to 50 even numbers
'''
sum_of_even = 0
for i in range(2,51,2):
    sum_of_even += i
print("Sum of even number from 1 to 50 is: ", sum_of_even)
