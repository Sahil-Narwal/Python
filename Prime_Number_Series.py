no = int(input("Enter the number till where you want to get the prime numbers : "))

for i in range(2, no):
    count = 0
    for x in range(1, i + 1):
        r = i % x
        if r == 0:
            count += 1
    if count == 2:
        print(i)
