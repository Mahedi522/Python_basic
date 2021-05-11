class A:

    def __init__(self):
        print("In A init")
    def feature1(self):
        print("Feature 1-A is working")

    def feature2(self):
        print("Feature 2 is working")


class B(A):
    def __init__(self):
        super().__init__()
        print("In B init")

    def feature1(self):
        print("Feature 1-B is working")

    def feature4(self):
        print("Feature 4 is working")


class X:
    def featurex1(self):
        print("Feature x1 is working")

    def featurex2(self):
        print("Feature x2 is working")


class C(A, X):

    def __init__(self):
        super().__init__()
        print("In C init")
    def feature5(self):
        print("Feature 5 is working")

    def feature6(self):
        print("Feature 6 is working")


    def feat(self):
        super().feature2()


a = C()
a.feature1()
a.feat()