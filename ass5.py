def is_self_dividing(n):
    list = str(n)
    for i in list:
        if n % int(i) == 0:
            return True
        else:
            return False

print(is_self_dividing(223))




