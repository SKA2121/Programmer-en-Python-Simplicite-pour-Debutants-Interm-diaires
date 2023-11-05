from abc import ABC, abstractmethod

class InstrumentMusical(ABC):
    def __init__(self, nom, coût_location):
        self.nom = nom
        self.coût_location = coût_location

    @abstractmethod
    def description(self):
        pass

class Guitare(InstrumentMusical):
    def __init__(self, nom, coût_location, type_guitare):
        super().__init__(nom, coût_location)
        self.type_guitare = type_guitare

    def description(self):
        return f"Guitare {self.nom} ({self.type_guitare}), Coût de location : {self.coût_location} € par mois"

class Piano(InstrumentMusical):
    def __init__(self, nom, coût_location, marque):
        super().__init__(nom, coût_location)
        self.marque = marque

    def description(self):
        return f"Piano {self.nom} ({self.marque}), Coût de location : {self.coût_location} € par mois"

class Batterie(InstrumentMusical):
    def __init__(self, nom, coût_location, modèle):
        super().__init__(nom, coût_location)
        self.modèle = modèle

    def description(self):
        return f"Batterie {self.nom} ({self.modèle}), Coût de location : {self.coût_location} € par mois"

# Utilisation des classes
guitare = Guitare("Acoustique", 30, "Classique")
piano = Piano("À queue", 50, "Yamaha")
batterie = Batterie("Électronique", 40, "Roland")

instruments = [guitare, piano, batterie]

for instrument in instruments:
    print(instrument.description())
