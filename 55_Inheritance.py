class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


class B(A):
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class X:
    def featurex1(self):
        print("Feature x1 is working")

    def featurex2(self):
        print("Feature x2 is working")


class C(B):
    def feature5(self):
        print("Feature 5 is working")

    def feature6(self):
        print("Feature 6 is working")

class D(B, X):
    def feature7(self):
        print("Feature 7 is working")

    def feature8(self):
        print("Feature 8 is working")

b1 = B()
b1.feature1()    # B inherits A (single level inheritance)

c1 = C()
c1.feature1()    # class C inherits class a and b(multi level inheritance)

d1 = D()
d1.featurex1()    # class d inherits 2 different class (multiple inheritance)
