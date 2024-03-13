"""
we are doing this because, apparently I can't think
"""
numbers = [2, 2, 1, 7, 4, 5, 5, 5, 5]

uniques = []

for n in numbers:
    if n not in uniques:
        uniques.append(n)

print(uniques)
