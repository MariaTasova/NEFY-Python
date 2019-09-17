def get_digit_sum(n):
    string_repr = str(abs(n))
    digits_sum = 0
    for digit in string_repr:
        digits_sum += int(digit)
    return digits_sum
print(get_digit_sum(-123))



