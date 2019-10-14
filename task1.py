def number_of_matches(J, S):
    J = set(J)
    counter = 0
    for i in S:
        if i in J:
            counter += 1
    return counter

print(number_of_matches("zZZZ", "ZZ"))

def number_of_matches(J, S):
    list = []
    for i in S:
        for j in J:
            if i == j:
                list.append(i)
    return len(list)

print(number_of_matches("aAb", "aAAbbb"))
