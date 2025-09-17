# Custom Exception for Salary Restriction
class SalaryAccessException(Exception):
    def __init__(self, message="Access Denied: Salary must be at least ₹1,00,000 to view car details."):
        self.message = message
        super().__init__(self.message)


# Car Class
class Car:
    def __init__(self, brand, model, price, fuel_type, transmission, color):
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__fuel_type = fuel_type
        self.__transmission = transmission
        self.__color = color

    # Encapsulation with getters
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def get_details(self):
        return {
            "Brand": self.__brand,
            "Model": self.__model,
            "Price": self.__price,
            "Fuel Type": self.__fuel_type,
            "Transmission": self.__transmission,
            "Color": self.__color
        }


# Showroom Class
class Showroom:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def view_cars(self):
        if not self.inventory:
            print("No cars available in the showroom.")
        else:
            print("\nAvailable Cars in Showroom:")
            for car in self.inventory:
                print(f"- {car.get_model()} ({car.get_brand()}) - ₹{car.get_price()}")

    def display_car_details(self, model, salary):
        try:
            if salary < 100000:
                raise SalaryAccessException()
            for car in self.inventory:
                if car.get_model().lower() == model.lower():
                    details = car.get_details()
                    print("\nCar Details:")
                    for key, value in details.items():
                        print(f"{key}: {value}")
                    return
            print("Car not found in inventory.")
        except SalaryAccessException as e:
            print(e)

    def sell_car(self, model):
        for car in self.inventory:
            if car.get_model().lower() == model.lower():
                self.inventory.remove(car)
                print(f"Car {model} sold successfully!")
                return
        print("Car not found in inventory.")

    def buy_car(self, car):
        self.inventory.append(car)
        print(f"Car {car.get_model()} added to inventory successfully!")


# Menu-driven interface
def main():
    showroom = Showroom("Dream Cars")

    # Preloaded cars
    showroom.buy_car(Car("BMW", "X5", 7500000, "Petrol", "Automatic", "Black"))
    showroom.buy_car(Car("Audi", "A6", 6000000, "Diesel", "Automatic", "White"))
    showroom.buy_car(Car("Toyota", "Innova", 2500000, "Diesel", "Manual", "Silver"))

    while True:
        print("\n--- Car Showroom Management System ---")
        print("1. View Available Cars")
        print("2. Display Car Details")
        print("3. Sell a Car")
        print("4. Buy a Car")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            showroom.view_cars()
        elif choice == "2":
            model = input("Enter car model name: ")
            salary = int(input("Enter your salary: "))
            showroom.display_car_details(model, salary)
        elif choice == "3":
            model = input("Enter car model to sell: ")
            showroom.sell_car(model)
        elif choice == "4":
            brand = input("Enter Car Brand: ")
            model = input("Enter Car Model: ")
            price = int(input("Enter Car Price: "))
            fuel = input("Enter Fuel Type: ")
            transmission = input("Enter Transmission: ")
            color = input("Enter Color: ")
            new_car = Car(brand, model, price, fuel, transmission, color)
            showroom.buy_car(new_car)
        elif choice == "5":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
