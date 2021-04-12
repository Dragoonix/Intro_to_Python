    #Task 2 Sample Solution
"""
Write a python program which accepts accepts the 
radius of a circle from the user and compute the area.
"""
_PI = 3.14
radius = int(input("Please enter the radius"))
area = _PI * radius**2
print("The area of a circle is : "+ str(area))
    #Task 3 Sample Solution
""" 
Using the same input, calculate the diameter and circumference of the circle and display your answer.
Add some comments to your program. Demonstrate your understanding of single line comments and multi-line 
comments.
 """
diameter = radius * 2
circumference = 2 * _PI * radius #this is the circumference
print("The diameter of a circle is :"+ str(diameter))
print("The circumference of a circle is :"+ str(circumference))