class Computer:
    def __init__(self):
        self.name = 'Mahedi'
        self.age = 22

    def update(self):
        self.age = 30

    def compare(self, other):
        if c1.age == c2.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

c1.name = "Romman"

c1.update()

if c1.compare(c2):
    print("They are equal")
else:
    print("not equal")

print(c1.name)
print(c2.name)
