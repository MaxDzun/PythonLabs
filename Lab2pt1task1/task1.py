# Task 1.
# Write a program for selling tickets to IT-events. Each ticket has a unique number and a price.
# There are four types of tickets: regular ticket, advance ticket (purchased 60 or more days before
# the event), late ticket (purchased fewer than 10 days before the event) and student ticket.
# Additional information:
# -advance ticket - discount 40% of the regular ticket price;
# -student ticket - discount 50% of the regular ticket price;
# -late ticket - additional 10% to the regular ticket price.
# All tickets must have the following properties:
# -the ability to construct a ticket by number;
# -the ability to ask for a ticket’s price;
# -the ability to print a ticket as a String.

import json
import uuid
from datetime import datetime, date

Late_ticket_factor = 1.1
Advance_ticket_discount = 0.6
Student_ticket_discount = 0.5

class Event_Ticket:
    def __init__(self, ticket_cost):
        self._ticket_cost = ticket_cost
        self._id = uuid.uuid4()

    @property
    def get_info(self):
        return self._ticket_cost, self._id

    @property
    def get_ticket_cost(self):
        return self._ticket_cost

    def __str__(self):
        return f"Price is: {self._ticket_cost}$\nTicket id is: {self._id}\n"

class Late_tick(Event_Ticket):
    def __init__(self, ticket_cost):
        super().__init__(ticket_cost)
        self._ticket_cost = round(self._ticket_cost / Late_ticket_factor)

class Advance_tick(Event_Ticket):
    def __init__(self, ticket_cost):
        super().__init__(ticket_cost)
        self._ticket_cost = round(self._ticket_cost * Advance_ticket_discount)


class Student_tick(Event_Ticket):
    def __init__(self, ticket_cost):
        super().__init__(ticket_cost)
        self._ticket_cost = round(self._ticket_cost * Student_ticket_discount)

class Ticket_seller:
    def __init__(self):
        self._event_chosen = ""
        self._ticket = ""

    def sell_event(self):
        with open("TicketsData.json", 'r', encoding="utf-8") as file:
            tickets_data = json.load(file)
        choice = input("Please, input event's type: ")
        if not any(x["type"] == choice for x in tickets_data["TicketsData"]):
            raise ValueError("Wrong type")
        for i in tickets_data["TicketsData"]:
            if choice == i["type"]:
                if i["amount"] <= 0:
                    raise ValueError("Tickets sold")
                i["amount"] -= 1
                json.dump(tickets_data, open("TicketsData.json", "w", encoding="utf-8"), indent=4)
                self._event_chosen = i.copy()

    @staticmethod
    def get_diff(event_date):
        data = datetime.now()
        current_date = (data.year, data.month, data.day)
        event_date = tuple(int(i) for i in reversed(event_date.split(".")))
        if current_date > event_date:
            raise TimeoutError("Ticket expired")
        return (date(data.year, data.month, data.day) - date(event_date[0], event_date[1], event_date[2])).days

    def order_ticket(self):
        ticket_type = input("\nChoose from tickets: standart, student, advanced, late\n Enter: ")
        days_difference = abs(Ticket_seller.get_diff(self._event_chosen["date"]))

        if not (ticket_type in ("standart", "student", "advanced", "late")):
            Ticket_seller.order_ticket(self)
        elif ticket_type == "standart":
            self._ticket = Ticket_seller(self._event_chosen["cost"])
        elif ticket_type == "late":
            if 0 <= days_difference < 10:
                self._ticket = Late_tick(self._event_chosen["cost"])
            else:
                raise TimeoutError(f"Ticket will be in {days_difference - 10} days")
        if ticket_type == "advanced":
            if days_difference >= 60:
                self._ticket = Advance_tick(int(self._event_chosen["cost"]))
            else:
                raise TimeoutError("No such ticket")
        elif ticket_type == "student":
            self._ticket = Student_tick(self._event_chosen["cost"])


        with open("SoldTickets.json") as file:
            database = json.load(file)
        if "Data" not in database:
            database["Data"] = {}
        ticket_id = str(self._ticket.get_info[1])
        if not (ticket_id in database["Data"]):
            database["Data"][ticket_id] = {
                "event": self._event_chosen["type"],
                "place": self._event_chosen["place"],
                "date": self._event_chosen["date"],
                "ticketType": ticket_type,
                "cost": self._ticket.get_price,
                "sellDate": str(datetime.now())
            }
            json.dump(database, open("SoldTickets.json", "w", encoding="utf-8"), indent=4)

    @property
    def get_price(self):
        return self._ticket.get_price

    @property
    def get_ev(self):
        tickets_data = json.load(open("TicketsData.json"))
        return "\n".join([f'Type: {event["type"]}\n '
                          f'Place: {event["place"]}\n'
                          f'Date: {event["date"]} '
                          f'\nCost: {event["cost"]}$\n' for event in tickets_data["TicketsData"]])

    def __str__(self):
        return f'\nType of event: {self._event_chosen["type"]}\t' \
               f'\nPlace of event: {self._event_chosen["place"]}\t' \
               f'Date of event: {self._event_chosen["date"]}\t' \
               f'\n\n{self._ticket}'

order = Ticket_seller()
print(order.get_ev)
order.sell_event()
order.order_ticket()
print(order)
