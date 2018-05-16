bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[0].upper())

#最后一个元素
print(bicycles[-1].title())

#倒数第二个元素（以此类推）
print(bicycles[-2].title())

print(bicycles[2-1].title())

message = "My first bicycle was a" + " " + bicycles[0].title()
print(message)