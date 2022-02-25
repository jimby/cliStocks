class Car:
    brand_name = "Chevy"
    model = "Galaxy"
    manu_year = "1946"

    def __init__(self, brand_name, model, manu_year):
        self.brand_name = brand_name
        self.model = model
        self.manu_year = manu_year

    def car_details(self):
        print("Car brand is ", self.brand_name)
        print("Car model is ", self.model)
        print("Car manufacture year is ", self.manu_year)
    
    def get_Car_brand(self):
        print("Car brand is ", self.brand_name)

    def get_Car_model(self):
        print("Car model is ", self.model) 

