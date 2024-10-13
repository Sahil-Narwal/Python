# To find that given mo. is palindrome or not

rem = 0
rev = 0
n = int(input("Enter the number : "))
m = n

while n > 0:
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10
if m == rev:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
