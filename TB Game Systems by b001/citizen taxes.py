citizens = [
    ('steve', 10),
    ('mark', 69),
    ('jack', 13)
]


def tax(Citizen):
    name = Citizen[0]
    taxed_balance = Citizen[1] * 0.93
    return name, taxed_balance


'''taxed_citizens = []
for citizen in citizens:
    taxed_citizen = tax(citizen)
    taxed_citizens.append(taxed_citizen)'''

# or use a built-in function called map like this :

taxed_citizens = list(map(tax, citizens))
# what it does is that it applies the function to each element in the iterable

print(taxed_citizens)
