class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class MyIde:
    def execute(self):
        print("Spell Check")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


ide1 = MyIde()

lap1 = Laptop()
lap1.code(ide1)