class Character():
    name = "jhon"
    fuerza = 0
    hp = 0
    mp = 0

    def __init__(self, name,fuerza,hp,mp) -> None:
        self.name = name
        self.fuerza = fuerza
        self.hp = hp
        self.mp = mp

    def at(self):
        print(self.name , "\tsus atributos son\n",
              "-fuerza:\t", self.fuerza,
              "\n-vida:\t",self.hp,
              "\n-magia:\t",self.mp)
    
    def update(self, fuerza, hp, mp):
        self.fuerza = self.fuerza + fuerza
        self.hp += hp
        self.mp += mp

if __name__ == "__main__":
    my_character = Character("frank", 120, 20,10)
    my_character.at()
    my_character.update(8,9,15)
    my_character.at()
    
