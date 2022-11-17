# Task 2.
# Pizzeria offers pizza-of-the-day for business lunch. The type of pizza-of-the-day depends on
# the day of week. Having a pizza-of-the-day simplifies ordering for customers. They
# don't have to be experts on specific types of pizza. Also, customers can add extra ingredients
# to the pizza-of-the-day. Write a program that will form orders from customers.
import json
from datetime import datetime as date

pizza_data = "PizzaOfTheDay.json"
extras_price = 3

class Pizza:
    def __init__(self, name, *ingredients):
        self.name = name
        with open(pizza_data, 'r', encoding="utf-8") as f:
            pizza_info = json.load(f)["todayspizza"][name]
        self.ingredients = pizza_info["ingredients"]
        self.price = pizza_info["price"]
        if ingredients:
            for additional in ingredients:
                self.price += extras_price
                self.ingredients[additional] = 1

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingr_name):
        if not isinstance(t, dict) or not ingr_name:
            raise TypeError("Wrong pizza ingredient")
        self.__ingredients = ingr_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def type(self, name):
        if not isinstance(name, str) or not name:
            raise TypeError("Wrong pizza name")
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(p, int) or isinstance(p, float) and price > 0:
            self.__price = price
        else:
            raise ValueError("Wrong pizza price")

class Todays_pizza(Pizza):
    def __init__(self, *ingredients):
        day = date.today().strftime("%A")
        match day:
            case "Monday":
                name = "Hawaiian"
            case "Tuesday":
                name = "Carbonara"
            case "Wednesday":
                name = "Francheska"
            case "Thursday":
                name = "Mushroom"
            case "Friday":
                name = "VegetaTeriyaki"
            case "Saturday":
                name = "Gorgonzola"
            case "Sunday":
                name = "ThaiChicken"
        super().__init__(name, *ingredients)
        with open(pizza_data, 'r', encoding="utf-8") as file:
            pizza_info = json.load(file)["pizzaoftheday"][name]
        self.price = int(pizza_info["price"]) * 0.5
        for x in ingredients:
            self.price += extras_price


class Pizza_Order:
    def __init__(self, customer_name, *args):
        self.customer_name = customer_name
        self.pizza = args

    @property
    def customer_name(self):
        return self.__customer_name

    @customername.setter
    def name(self, customer_name):
        if not isinstance(customer_name, str) or not customer_name:
            raise TypeError("Wrong customer name")
        self.__customer_name = customer_name

    def total_order_bill(self):
        p = 0
        print("Name: " + self.name)
        for x in self.pizza:
            print(x.name + " with ingredients: ", x.ingredients)
            p += x.price
        print("Total price: ", p)

PizzaOfTheDayOrder = Todays_pizza("mushrooms")
InDetailsOrder = Pizza("54 cheese", "tomatoes", "mushrooms", "meat")
TotalOrder = Pizza_Order("Donatello", PizzaOfTheDayOrder, InDetailsOrder)
TotalOrder.total_order_bill()