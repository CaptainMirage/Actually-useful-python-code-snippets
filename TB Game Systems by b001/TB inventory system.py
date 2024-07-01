# inventory management system thingy

inventory = ['Awkward Sword', 'Superior Shield', 'Hunter Bow', 'stick']
rarity = {
    'Awkward Sword': 98,
    'Superior Shield': 90,
    'Hunter Bow': 80,
    'axe': 69,
    'stick': 13
}

sort_inv = sorted(inventory, key=rarity.__getitem__, reverse=True)
print(sort_inv)
