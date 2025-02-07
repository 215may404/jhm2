while is true:
a = float(input("Input the height of a student 1 in cm:"))
b = float(input("Input the height of a student 2 in cm:"))
c = float(input("Input the height of a student 3 in cm:"))
d = float(input("Input the height of a student 4 in cm:"))
  if a or b or c or d < 0:
    print("Height must be positive."）
  elif a or b or c or d > 200:
    print("Height is greater than 200cm.")
  elif 0 < a or b or c or d > 200:
    print("End of input.")
    break
  else：
    print("Error")
values = [a, b, c, d]
print("The average height of these students is {float(average(values))} cm.")
print("The maximum height of these students is {float(max(values))} cm.")
