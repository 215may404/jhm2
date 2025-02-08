size = int(input("Input Addition Table Size smaller 10:"))
if size < 10:
    print("Addition Table")
    print('-------------------------------------------------------')
    for i in range(1,size+1):
        for j in range(1,size+1):
            print(f"{i} + {j} = {i+j:2}",end="  " )
        print()
    print('-------------------------------------------------------')
else:
    print("wrong answer")
