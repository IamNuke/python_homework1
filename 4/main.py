n = int(input("n = "))
m = int(input("m = "))
k = int(input("k = "))
if k > n * m:
    print("Wrong parameters")
else:
    if k % n == 0 or k % m == 0:
        print("yes")
    else:
        print("no")

