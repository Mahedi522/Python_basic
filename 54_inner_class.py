class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "hp"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Mahedi", 1)
s2 = Student("Romman", 2)

s1.show()
s2.show()

print(s1.lap.brand)
lap1 = s1.lap
lap2 = s2.lap

lap3 = Student.Laptop()
