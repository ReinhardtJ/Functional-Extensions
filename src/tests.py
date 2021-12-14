input = [5, 3, 1, 8, 4]
copied = input.copy()
copied.sort() # looks good, let's continue
squared = map(lambda x: x**2, copied)
filtered = filter(lambda x: x % 2 == 0, squared)
result = filtered
for r in result:
    print(r)


input = [5, 3, 1, 8, 4]
filtered = [x ** 2 for x in input if x ** 2 % 2 == 0]
filtered.sort()
for entry in filtered:
    print(entry)