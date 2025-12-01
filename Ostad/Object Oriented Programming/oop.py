class car:
    def __init__(self,name,brand,model):
        self.name= name
        self.brand= brand
        self.model= model
    def start(self):
        print(f"{self.name} is starting.")  
    def stop(self):
        print(f"{self.name} is stopping.")

my_car= car("MyCar","Toyota","2020")
my_car.start()  
my_car.stop()
