import os
def rows_generator(file):
    with open(file, "r") as file:
        for line in file:
            yield line.strip()

gen = rows_generator("/home/maria/Документы/test3.txt")
for i, line in enumerate(gen):
    print(line)
    if i > 50:
        break
