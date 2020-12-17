class Vehicle:
    # Noun: Wheels, doors, engine, color, plate_number
    # Verb: reverse, park, start, honk
    def __init__(self, wheels, doors, engine, color, plate_number, model):
        self.wheels = wheels
        self.doors = doors
        self.engine = engine
        self.plate_number = plate_number
        self.model = model
    def reverse(self):
        return "The car is reversing!"

    def park(self):
        return "Skreech"

    def start(self):
        return "VROOOM!!!"

    def honk(self):
         return "PEEEEEPEEEE!!!!"   

class Lorry(Vehicle):
    def __init__(self, wheels, doors, color, engine, plate_number, model, container ):
        Vehicle.__init__(self, wheels, doors, color, engine, plate_number, model)
        self.container = container

lorry2 = Vehicle(wheels = 4, doors= 4, engine = "Diesel", color = "Black", plate_number = "KBX 123", model = "Lorry")
pikipiki = Vehicle(wheels= 2, doors = 0, engine = "Petrol",  color = "Red", plate_number = "XRTF 454", model = "Motorbike")
trailer = Vehicle(wheels = 8, doors = 2, engine = "Diesel", color= "Orange", plate_number="KBB 675", model = "Trailer")

lorry1 = Lorry(wheels = 4, doors = 2, color = "Pink", plate_number = "KBG 567", engine= "Diesel", model = "ivehicle", container = 1 )
print("The tailer has {} wheels" .format(trailer.wheels))
print("The pikipiki has {} wheels" .format(pikipiki.wheels))
print(lorry1.honk())
          