print("This is first module")

def main():
    print("Hello World!")
    print(__name__)


def functionFromFirstMod():
    a = 10
    print(a)

variable = 11


if __name__ == '__main__':
    main()