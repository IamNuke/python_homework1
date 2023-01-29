summ = int(input("Enter total summ:"))

if (summ % 6) == 0:
    a = int(summ/6)
    b = a
    c = 2 * (a+b)
    print(f"{a} {b} {c}")
else:
    print("wrong parameter")