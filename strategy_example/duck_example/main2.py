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


class GenericTamagoshi():

    def __init__(self, tipo, sleepBehavior, playBehavior, eatBehavior):
        self.tipo = tipo
        self.sleepBehavior = sleepBehavior
        self.playBehavior = playBehavior
        self.eatBehavior = eatBehavior

    def sleep(self):
        self.sleepBehavior()

    def play(self):
        self.playBehavior()

    def eat(self):
        self.eatBehavior()

    def reproduce(self, sleepBehavior, playBehavior, eatBehavior):
        return GenericTamagoshi(self.tipo, sleepBehavior, playBehavior, eatBehavior)



def FantasmaSleepBehavior():
    print("Fantasma sleeping")

def FantasmaPlayBehavior():
    print("Booo!")

def NoEatBehavior():
    return None

def RoboSleepBehavior():
    print("Robô sleeping")

def RoboPlayBehavior():
    print("Bzzz!")

def StadByBehavior():
    print("Stand by")

def RoboEatBehavior():
    print("Reacharging...")


if __name__ == "__main__":
    

    # tamagoshi = Tamagoshi("Tamagoshi", 100, 100)
    # tamagoshi.eat()
    # tamagoshi.sleep()
    # tamagoshi.play()

    # tipo = "Fantasma"
    # sleepBehavior = FantasmaSleepBehavior
    # playBehavior = FantasmaPlayBehavior
    # eatBehavior = NoEatBehavior

    # tipo = "Robo"
    # sleepBehavior = StadByBehavior
    # playBehavior = RoboPlayBehavior
    # eatBehavior = RoboEatBehavior

    caracteristicas = {
        "Fantasma": {"tipo": "Fantasma", "sleepBehavior": FantasmaSleepBehavior, "playBehavior": FantasmaPlayBehavior, "eatBehavior": NoEatBehavior},
        "Robo": { "tipo": "Robo", "sleepBehavior": RoboSleepBehavior, "playBehavior": RoboPlayBehavior, "eatBehavior": RoboEatBehavior}
    }

    caracteristica = caracteristicas.get("Robo")



    custonSleepBehavior = {
        "Fantasma": FantasmaSleepBehavior,
        "Robo": RoboSleepBehavior,
        # ...

    }


    custonPlayBehavior = {
        "Fantasma": FantasmaPlayBehavior,
        "Robo": RoboPlayBehavior,
        # ...
    }


    custonEatBehavior = {
        "Fantasma": NoEatBehavior,
        "Robo": RoboEatBehavior,
        # ...
    }


    caracteristica["sleepBehavior"] = custonSleepBehavior.get("Robo")
    caracteristica["playBehavior"] = custonPlayBehavior.get("Fantasma")
    caracteristica["eatBehavior"] = custonEatBehavior.get("Fantasma")



    generic = GenericTamagoshi(caracteristica["tipo"], 
                               caracteristica["sleepBehavior"], 
                               caracteristica["playBehavior"], 
                               (caracteristica["eatBehavior"])
    )

    generic.sleep()
    generic.play()
    generic.eat()

