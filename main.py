usrInput = int(input("Enter a number: "))
count = 0

for i in range(1, usrInput + 1):
    if usrInput % i == 0:
        count = count + 1

if count == 2:
    print("Its a prime number")
else:
    print("Its not a prime number")