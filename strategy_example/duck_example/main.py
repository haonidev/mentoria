

class Tamagoshi:

    def __init__(self, name, food, mood):
        self.name = name
        self.food = food
        self.mood = mood

    def eat(self):
        self.food += 10

    def sleep(self):
        self.mood += 20
        self.food -= 10

    def play(self):
        self.mood += 5
        self.food -= 10

class Fantasma(Tamagoshi):
    
        def __init__(self, name, food, mood):
            super().__init__(name, food, mood)
    
        # def eat(self):
        #     self.food += 10
    
        def sleep(self):
            self.mood += 20
            self.food -= 10
    
        def play(self):
            self.mood += 5
            self.food -= 10


class Dinosauro(Tamagoshi):

    def __init__(self, name, food, mood):
        super().__init__(name, food, mood)

    def eat(self):
        self.food += 10

    def sleep(self):
        self.mood += 20
        self.food -= 10

    # def play(self):
    #     self.mood += 5
    #     self.food -= 10


class Robo(Tamagoshi):

    def __init__(self, name, food, mood):
        super().__init__(name, food, mood)

    def eat(self):
        self.food += 10

    # def sleep(self):
    #     self.mood += 20
    #     self.food -= 10

    def play(self):
        self.mood += 5
        self.food -= 10

class Cachorro(Tamagoshi):

    def __init__(self, name, food, mood):
        super().__init__(name, food, mood)

    def eat(self):
        self.food += 10

    def sleep(self):
        self.mood += 20
        self.food -= 10

    def play(self):
        self.mood += 5
        self.food -= 10
    



if __name__ == "__main__":
    

    tamagoshi = Tamagoshi("Tamagoshi", 100, 100)

    tamagoshi.eat()

    tamagoshi.sleep()

    tamagoshi.play()