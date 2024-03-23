class Car:
    def __init__(self):
        self.cgst=5555
        self.sgst=5555
        self.insurance=5555
    def company(self):
        while True:
            print("Toyota,Mercedes")
            self.n=input("enter the car company")
            if self.n=="Toyota":
                print("welcome to toyo")
                self.model()
                break
            elif self.n=="Mercedes":
                print("welcome to merc")
                self.model()
                break
            else:
                print("enter valid number")
    def model(self):
        if self.n=="Toyota":
            while True:
                print("select from Fortuner and LC")
                self.choice=input("Enter the car name")
                if self.choice(self.choice)
                break
            
