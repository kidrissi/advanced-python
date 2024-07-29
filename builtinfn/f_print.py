print("Python", "version", "3.0", sep="-")  # Output: Python-version-3.0
print("Hello", end="-")
print("World!")  # Output: Hello World!
print(type(repr([1, 2, 3])))  # Output: <class 'str'>


#

def generate_numbers(n):
    for i in range(n):
        yield i


gen = generate_numbers(5)
print(*gen)  # Output: 0 1 2 3 4