class Game():
    def __init__(self):
        self.var1 = 1
        self.var2 = 2
        self.var3 = 3
        self.cannon = Cannon()
    
    def func1(self):
        return self.var1
class Cannon(Game):
    def __init__(self):
        self.var1 = 4
        self.var2 = 5
        self.var3 = 6
        self.var4 = self.func1()
        #print(self.var1)
    
if __name__ == "__main__":
    game = Game()
