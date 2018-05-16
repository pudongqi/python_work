squares = []
for value in range(1,10):
	squares.append(value**2)
print(squares)

digits = range(1,10000,23)
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**3 for value in range(1,11)]
print(squares)