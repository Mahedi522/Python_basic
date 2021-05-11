from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(.5)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(.5)


t1 = Hello()
t2 = Hi()

# t1.run()
# t2.run()

t1.start()
sleep(.2)
t2.start()

t1.join()
t2.join()

print("Bye")
