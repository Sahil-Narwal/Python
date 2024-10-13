max1 = int(input("To which max you want to print fabonacci series: "))
first = 0
second = 1
next1 = 0
print("The fabonic series is ")
print(first)
print(second)

i = 0
for i in range(0, max1):
    next1 = first + second
    if next1 > max1:
        break
    first = second
    second = next1
    print(next1)
