def is_self_dividing(n):
    list = str(n)
    count = 0
    for i in range(0, len(list)):
        if n % int(list[i]) == 0:
            count += 1
    if count == len(list):
        return True
    else:
        return False

print(is_self_dividing(315))




