i = 0
m = 0
remainder = 0
cube = 0
n = int(input("Enter the number : "))

for i in range(1, n):
    m = i
    cube = 0
    while m > 0:
        remainder = m % 10
        cube = cube + (remainder * remainder * remainder)
        m = m // 10
    if i == cube:
        print(cube)
