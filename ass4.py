def is_prime(n):
    for number in range(2, abs(n)):
        if abs(n) % number == 0:
            return False
        else:
            return True


print(is_prime(17))



