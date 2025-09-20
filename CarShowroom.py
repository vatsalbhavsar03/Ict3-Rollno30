# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 05:45:18 2025

@author: Vatsal
"""
import pandas as pd
import numpy as np


class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_details(self):
        return {
            "Brand": self.brand,
            "Model": self.model,
            "Price": self.price
        }


class Showroom:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)
        print("✅ Car Added")

    def delete_car(self, model):
        for car in self.inventory:
            if car.model.lower() == model.lower():
                self.inventory.remove(car)
                print("🚗 Car Sold")
                return
        print("❌ Car not found")

    def view_car(self):
        if not self.inventory:
            return print("No cars available")
        df = pd.DataFrame([c.get_details() for c in self.inventory])
        print(f"\nAvailable cars in {self.name}\n", df)
        print("\nAverage Price:", df["Price"].mean())

    def display_details(self, model):
        for car in self.inventory:
            if car.model.lower() == model.lower():
                print("\nCar Details:\n", pd.Series(car.get_details()))
                return
        print("❌ Not found")


if __name__ == "__main__":
    showroom = Showroom("SuperCars")

    showroom.add_car(Car("BMW", "A1", 15000))
    showroom.add_car(Car("Audi", "O1", 20000))
    showroom.add_car(Car("Mahindra", "KK", 1500000))

    while True:
        print("\n========= Car Showroom =========")
        print("1. Show all")
        print("2. Display details")
        print("3. Sell car")
        print("4. Buy car")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            showroom.view_car()

        elif choice == "2":
            model = input("Enter car model: ")
            showroom.display_details(model)

        elif choice == "3":
            model = input("Enter car model to sell: ")
            showroom.delete_car(model)

        elif choice == "4":
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            try:
                price = float(input("Enter price: "))
                showroom.add_car(Car(brand, model, price))
            except ValueError:
                print("❌ Invalid price. Must be a number.")

        elif choice == "5":
            print("👋 Exiting Showroom System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")
