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
avg = np.average(heights)
height = np.max(heights)
print(f"The average height of these students is {"%.2f" % avg} cm.")
print(f"The maximum height of these students is {"%.2f" % height} cm.")
