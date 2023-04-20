input()
numbers = {}
for number in input().split():
    number = int(number)
    if number not in numbers:
        numbers[number] = 0
    else:
        numbers[number] += 1

most_frequent = max(numbers.values())
result = []
for number in numbers:
    if numbers[number] == most_frequent:
        result.append(number)

result.sort()

print(' '.join(str(n) for n in result))
