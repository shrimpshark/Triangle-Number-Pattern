def pyramid(row_num):
    k = row_num
    for i in range(row_num):
        i += 1
        row_count = (i - 1) * 2 + 1
        print((k - 1) * " ",end="")
        for j in range(row_count):
            j = j % 10
            print(j, end="")
        k -= 1
        print("")

while True:
    row_num = int(input("Enter num: "))
    if row_num <= 0:
        print("Invalid input")
    else:
        print("")
        pyramid(row_num)
        break