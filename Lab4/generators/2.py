def generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter number: "))
even_numbers = list(generator(n))
print(", ".join(map(str, even_numbers)))