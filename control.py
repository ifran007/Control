# #1. Largest Number
# a = int (input ("Please enter your 1st number: "))
# y = int (input ("Please enter your 2nd number: "))
# z = int (input ("Please enter your 3rd number: "))
# p = int (input ("Please enter your 4rd number: "))

# if (a > y and a > z and a > p ):
#     print(f'The highest number is {a}') 
# elif (y > z and y > p ):
#     print(f'The highest number is {y}')
# elif z > p:
#     print(f'The highest number is {z}')
# else:
#     print(f'The highest number is {p}')

#2. Exchange variable
# s = 12
# t = 13
# u = 14
# v = 15
# s = int (input ("Please enter your 1st number: "))
# t = int (input ("Please enter your 2nd number: "))
# u = int (input ("Please enter your 3rd number: "))
# v = int (input ("Please enter your 4rd number: "))
# tem = t
# tem_2 = u
# t = s
# s = v
# u = tem
# v = tem_2
# print("\n",s, "\n",t, "\n",u, "\n",v)

# #3.Area of rectangle
# lenght = int(input("Please enter the lenght of the rectangle: "))
# width = int(input("Please enter the width of the rectangle: "))
# if lenght > width:
# print( "The area of the rectangle is", lenght * width)

#4. Grade System
num = int(input("Please enter the marks: "))
if num > (100 or num < 0): 
    print("\n It Is not possible !!")
elif num >=80 :
    print ("\n You get A+")
elif 75 <= num <=79 :
    print ("\n You get A")
elif 70 <= num <= 74:
    print ("\n You get A-")
elif 65 <= num <=69 :
    print ("\n You get B+")
elif 60 <= num <=64:
    print ("\n You get B")
elif 55 <= num <=59 :
    print ("\n You get B-")
elif 50 <= num <= 54:
    print ("\n You get C+")
elif 45 <= num <=49 :
    print ("\n You get C")
elif 40 <= num <=44:
    print ("\nYou get D")
else:
    print("\n You fail")


# #IS_Operator
# x = ["apple", "banana"]
# y = ["mango", "orange"]
# z = x
# print("\n This  'IS' Operator Value:", x is z )
# print("\n This  'IS' Operator Value:", x is y )

# #IS_Not_Operator
# x = ["apple", "banana","pinaapple"]
# y = ["mango", "orange"]
# z = x
# print("\n This Is IsNotOperator Value:", x is not z, x is not y)