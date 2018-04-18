# File:      ricky_C_Portfolio_Exercise_1.py
# Author:    ricky chen
import math
print("This programm is made for Circle calculator!")
r = float(input("pls enter radius in centimeter"))
print("Operating....")
print("")
print('The diameter is ', r*2 , 'cm.')
c = float(2*math.pi*r)
print('The circumference is ',format(c ,'.4f') , "cm.")
S = float(r**2*math.pi)
print("The area is ", format(S,'.3f') , "cm.")
print("Thank for using Circle calculator.")

