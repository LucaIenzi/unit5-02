# Created by: luca.ienzi
# Created on: nov 2017
# Created for: ICS3U
# this program will randomly generate a input amount number and then find the max of the sum of the numbers
from numpy import random 


random_number = []

print("input a number ")
def calulate (number):
    for count in range(number):
        random_number.append(random.randint(10,100))
        
    
    return random_number
    


calulate(input())

print(random_number)


print(max(random_number))
