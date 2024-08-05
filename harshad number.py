num = int(input("Enter the number:"))
sum = 0
temp = num  # Assign num to temp for correct calculation
while temp > 0:
    digit = temp % 10
    sum += digit
    temp = temp // 10
if num % sum == 0:
    print("Harshad number")
else:
    print("Not a Harshad number")
