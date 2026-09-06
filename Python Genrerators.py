# -------------------------------
# Example 1: Using next() with a Generator
# -------------------------------

def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count
        count += 1

# Initialize the generator
counter = count_up_to(3)

# Retrieve values using next()
print(next(counter))
print(next(counter))
print(next(counter))


# -------------------------------
# Example 2: Simple Generator
# -------------------------------

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)


# -------------------------------
# Example 3: Count Up To n
# -------------------------------

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)


# -------------------------------
# Example 4: Generate Powers of 2
# -------------------------------

def PowTwoGen(max_power):
    n = 0
    while n < max_power:
        yield 2 ** n
        n += 1

# User Input
max_power = int(input("Enter the number of powers of 2 to generate: "))

print("Powers of 2 are:")
for value in PowTwoGen(max_power):
    print(value)
