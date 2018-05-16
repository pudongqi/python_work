cars = ['BMW', 'AUDI', 'TOYOTA', 'SUBARU']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))#倒序

print("\nHere is the original list:")
print(cars)

#永久排序
cars.sort()
print("\n" + str(cars))

#倒着打印,永久的
cars.reverse()
print("\n" + str(cars))


print(len(cars))



