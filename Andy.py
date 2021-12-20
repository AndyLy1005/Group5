# Hình 1.
n = 0
while n >= 0:
    n = int(input("Nhập kích thước hình: "))
    if n <= 0:
        print("Vui lòng nhập lại n > 0!")
    for row in range(n):
        for col in range(2*n):
            if row + col <= n-1:
                print("* ", end= " ")
            elif row + col >= 2*n-1:
                print("* ", end=" ")
            elif col == n:
                print("* ", end=" ")
            else:
                print(" ", end=" ")
        print()
