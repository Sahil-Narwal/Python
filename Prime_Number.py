i = int(input("Enter the number to check : "))

count = 0

for x in range(1, i + 1):
    r = i % x
    if r == 0:
        count += 1
if count == 2:
    print("The number is a prime number")
else:
    print("The number is not a prime number")

"""
for x in range(1, i + 1):
    if i % x == 0:
        count += 1
"""
