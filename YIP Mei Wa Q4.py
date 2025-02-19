import numpy as np
heights = []
for i in range (1,5):
    while True:
        heights = float(input(f"Input the height of a student {i} in cm:"))
        if (heights < 0):
            print("Height must be positive.")
        elif (heights > 200):
            print("Height is greater than 200cm.")
        else:
            break
print("End of input.")
avg = np.average(round(heights,2))
height = np.max(round(heights,2))
print(f"The average height of these students is {avg} cm.")
print(f"The maximum height of these students is {height} cm.")
