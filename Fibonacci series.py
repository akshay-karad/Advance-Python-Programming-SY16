# Fibonacci Series (Board Logic)

n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

if n >= 1:
    print(a)

if n >= 2:
    print(b)

for i in range(2, n):
    c = a + b + 1
    print(c)
    a = b
    b = c
