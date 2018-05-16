#切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])

for player in players[:3]:
	print(player.title())


values = list(range(1,10000))
print(values[-3:])


lists = [1,2,3,4,5,6,7,8,9]
lists.sort( reverse = True )
print(lists[:3])

