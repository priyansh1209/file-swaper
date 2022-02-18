def swapPrinch():
    file1 = input("Enter the path of file 1 ")
    file2 = input("Enter the path of file 2 ")

    with open(file1, 'r') as a:
        data1 = a.read()

    with open(file2, 'r') as b:
        data2 = b.read()

    with open(file1, 'w') as a:
        a.write(data2)

    with open(file2, 'w') as b:
        b.write(data1)

#-------------------------------------

    with open(file1, 'r') as a:
        show1 = a.read()

    with open(file2, 'r') as b:
        show2 = b.read()

    print("New Content ---> ")
    print("data in File 1 --> " , show1)
    print("data in File 2 --> " , show2)

swapPrinch()