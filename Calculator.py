import math
print("######CALCULATOR######")
selection=int(input("Choose 1 for Basic Calculator. Choose 2 for trigonometric calculator "))
if selection==1:
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    print("Enter + for addition")
    print("Enter - for addition")
    print("Enter * for addition")
    print("Enter / for addition")
    print("Enter ^ for addition (a is base, b is power)")


    op=input("Enter the operator")
    if op=="+":
        r=a+b
    elif op=="-":
        r=a-b
    elif op=="*":
        r=a*b
    elif op=="/":
        r=a/b
    elif op=="^":
        r=a**b
    else:
        print("Check the operator")
    print("Result is", r)

if selection==2:
    print("Enter 1 for sine")
    print("Enter 2 for cosine")
    print("Enter 3 for tan")
    print("Enter 4 for cosec")
    print("Enter 5 for sec")
    print("Enter 6 for cot")
    n=int(input("Enter the operator"))
    x=float(input("Enter angle in radians"))
    if n==1:
        print(math.sin(x))
    elif n==2:
        print(math.cos(x))
    elif n==3:
        print(math.tan(n))
    elif n==4:
        print(math.asin(x))
    elif n==5:
        print(math.acos(x))
    elif n==6:
        print(math.atan(n))
    else:
        print("Check the operator")
  
