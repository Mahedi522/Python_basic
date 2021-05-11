names = ("Mahedi", "Evan", "Romman")
comps = ("Apple", "Google", "Samsung")

zipped = list(zip(names, comps))
print(zipped)

zipped = set(zip(names, comps))
print(zipped)

zipped = dict(zip(names, comps))
print(zipped)
