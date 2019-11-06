#object creation#
class Bot:
    def __init__(self, name, age, energy, shield):
        self.name = name
        self.age = str(age)
        self.energy = int(energy)
        self.shield = str(shield)
    
    def display_name(self):
        print("███████")
        print("█"+ self.name +"█")
        print("███████")
    def display_age(self):
        print("   " + self.age + "   ")
        print("  ███  ")
        print(" █████ ")
        print("███████")
    def display_energy(self):
        print ("Energy:" + "█" * self.energy)
    def display_shield(self):
        print("████████")
        print(" ██"+ self.shield +"██ ")
        print("  ████")
    def display_summary(self):
        print("the bot, {} , is {} years old. its energy level is {} and it has a shield level of {}".format(self.name, self.age, self.energy, self.shield))


#assigning values #
sassy = Bot("Sassy",20, 10, 50)

sassy.display_name()
sassy.display_age()
sassy.display_energy()
sassy.display_shield()
sassy.display_summary()

