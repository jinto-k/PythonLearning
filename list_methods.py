numbers = [2, 2, 1, 7, 4, 5,5,5,5,5]
another = [1, 2, 3, 45]
numbers.append(13)
numbers.insert(0, 12)
numbers.remove(2)  # numbers.remove removes the actual value not the index. and apparently only one 2
numbers.pop()  # removes the last element of the list

print(numbers.index(2))
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()  # sort in descending order
print(numbers)

numbers2 = numbers.copy()
print(numbers2)

another.clear()

print(another)
