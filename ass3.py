def is_power_of_two(n):
    while n >= 2:
        n = n / 2
    if n == 1.0:
        return(True)
    else:
        return(False)

print(is_power_of_two(12))




