lst = [3, 2, 10, 15, 11, 13, 17, 35, 50, 55, 91, 100]
prime = []

for num in lst:
    if num < 2:
        continue
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        prime.append(num)

if len(prime) > 0:
    print('Prime numbers:', prime)
else:
    print("No prime number in the list")

