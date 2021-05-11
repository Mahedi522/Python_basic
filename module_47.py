def add():
    print("Result of add from modules", __name__)


def sub():
    print("Result of sub from modules", __name__)


def mul():
    print("Result of mul from modules", __name__)


def div():
    print("Result of div from modules", __name__)


def main():
    add()
    mul()
    sub()
    div()


if __name__ == "__main__":
    main()
