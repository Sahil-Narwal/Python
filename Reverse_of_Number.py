rem = 0
rev = 0
n = int(input("Enter the number : "))
m = n

while n > 0:
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10

print("The reverse of ", m, " is: ", rev)
