# players inventory with the corresponding data value
items = [
    'Mystic Sword',
    'wooden pickaxe',
    'rock'
]

rarity = [
    99,
    56,
    9
]

weight = [
    1.30,
    1.10,
    0.01
]

inv = zip(items, rarity, weight)
print(list(inv))

# for unzipping

# i, r, w = zip(*inv)
# print(i, r, w)
