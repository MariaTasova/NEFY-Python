def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        return True

print(is_prime(144))

#You do not actually need to go all the way up to n if you want to check if n is a prime number. You can dramatically reduce the tests and only check from 2 to √(n)




