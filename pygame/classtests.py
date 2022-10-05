class Main:

    def __init__(self):
        self.main()
        self.var1 = 1

    def main(self):
        print("Hello World")

class NotMain:
    def __init__(self):
        self.main()
        self.var2 = 2

    def main(self):
        print("Hello World")
        self.var2 = main.var1

if __name__ == "__main__":
    main = Main()
    notmain = NotMain()