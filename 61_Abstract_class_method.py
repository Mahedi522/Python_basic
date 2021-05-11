from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        print("abstract class Running")


class Laptop(Computer):
    pass

c = Computer()
c.process()
