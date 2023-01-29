

number = int(input("Enter number:"))

if (int(number / 1000) == 0) and (int(number / 100) > 0):
    result = (number % 10) + int(number/10 % 10) + int(number/100 % 10)
    print(f"Summ: {result}")
else:
    print("wrong parameter")