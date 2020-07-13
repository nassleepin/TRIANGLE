# TRIANGLE

a = int(input("please enter the length of the side of the triangle:"))
while a < 0:
    a = int(input("please re-enter the length of the side of the triangle with a suitable length"))


b = int(input("please enter the length of the other side of the triangle:"))
while b < 0:
    b = int(input("please re-enter the length of the side of the triangle with a suitable length")) 


c = int(input("please enter the length of the last side of the triangle:"))
while c < 0:
    c = int(input("please re-enter the length of the side of the triangle with a suitable length"))




if a == b and b == c:
    if (a > b and a > c and a > ( b + c)) or (c > b and c > a and c > ( a + b )) or (b > a and b > c and b > ( a + c)):
        print("The dimensions provided cannot form a triangle.")
    else:
        print("You have enetered an equilateral triangle.")
        if (a**2 == b **2 + c **2) or (b**2 == a **2 + c **2) or (c**2 == b **2 + a **2):
            print("Triangle is also a right-angled triangle")
        elif (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2) or (c**2 > b**2 + a**2):
            print("Triangle is also an obtuse triangle")

elif (a == b and a != c) or (a == c and c != b) or (b == c and a != c):
    if (a > b and a > c and a > ( b + c)) or (c > b and c > a and c > ( a + b )) or (b > a and b > c and b > ( a + c)):
        print("The dimensions provided cannot form a triangle.")
    else:
        print("You have entered an isosceles triangle.")
        if (a**2 == b **2 + c **2) or (b**2 == a **2 + c **2) or (c**2 == b **2 + a **2):
            print("Triangle is also a right-angled triangle")
        elif (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2) or (c**2 > b**2 + a**2):
            print("Triangle is also an obtuse triangle")

elif a != b and b != c:
    if (a > b and a > c and a > ( b + c)) or (c > b and c > a and c > ( a + b )) or (b > a and b > c and b > ( a + c)):
        print("The dimensions provided cannot form a triangle.")
    else:
        print("You have entered a scalene triangle.")
        if (a**2 == b **2 + c **2) or (b**2 == a **2 + c **2) or (c**2 == b **2 + a **2):
            print("Triangle is also a right-angled triangle")
        elif (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2) or (c**2 > b**2 + a**2):
            print("Triangle is also an obtuse triangle")
