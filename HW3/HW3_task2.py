def divider_generator(number):
    for i in range(1, number+1):
        if number % i == 0:
            yield i

dividers = divider_generator(1024)
for i in dividers:
    print(i)
