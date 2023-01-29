number = int(input("Enter number:"))
if number // 100000 > 0:
    first_part = number // 1000
    second_part = number % 1000
    first_sum = (first_part % 10) + int(first_part/10 % 10) + int(first_part/100 % 10)
    second_sum = (second_part % 10) + int(second_part / 10 % 10) + int(second_part / 100 % 10)
    if first_sum == second_sum:
        print("yes")
    else:
        print("no")
else:
    print("wrong parameter")