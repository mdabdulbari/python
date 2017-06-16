stuff = {'name': 'Bari', 'age': 21, 'height': 5 * 12 + 6}
stuff[1] = "wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2])
stuff['city'] = "HYD"

del stuff['city']
del stuff[1]
del stuff [2]
print(f"{stuff}")
