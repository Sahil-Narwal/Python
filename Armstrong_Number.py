n = int(input("Enter the number"))
m = n
rem = 0
cube = 0

while n > 0:
    rem = n % 10
    cube += rem * rem * rem
    n = n // 10
if m == cube:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")
