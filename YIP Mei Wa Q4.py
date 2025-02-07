while True:
    a = float(input("Input the height of a student 1 in cm:")),
    if a < 0:
        print("Height must be positive.")
    elif a > 200:
        print("Height is greater than 200cm.")
    else:
        print("Error")
    b = float(input("Input the height of a student 2 in cm:")),
    if b < 0:
        print("Height must be positive.")
    elif b > 200:
        print("Height is greater than 200cm.")
    else:
        print("Error")
    c = float(input("Input the height of a student 3 in cm:")),
    if c < 0:
        print("Height must be positive.")
    elif c > 200:
        print("Height is greater than 200cm.")
    else:
        print("Error")
    d = float(input("Input the height of a student 4 in cm:")),
    if d < 0:
        print("Height must be positive.")
    elif d > 200:
        print("Height is greater than 200cm.")
    else:
        print("Error")
        break
values = [a,b,c,d]
print("End of input.")
print("The average height of these students is {float(average(values))} cm.")
print("The maximum height of these students is {float(max(values))} cm.")
