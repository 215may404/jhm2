range_limit = int(input("Input Addition Table Size smaller 10:"))
for i in range(1, range_limit + 1):
    for j in range(1, range_limit + 1):
        print(f"{i + j:2}",end="")
