# Class method
# Static method
# instance method

class Student:
    school = "BZS"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):                  #Instance method (passing sef)
        return(self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def getSchool(cls):             # class method
        return cls.school

    @staticmethod
    def info():                  # Static method
        print("This is a static method")


s1 = Student(23, 43, 55)
s2 = Student(43, 54, 76)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())

Student.info() 

