# Lesson 8 tasks 4, 5, 6

from abc import ABC, abstractmethod


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg


class Warehouse:

    def __init__(self):
        self.stock = dict()

    @property
    def key_list(self):
        return [_ for _ in self.stock.keys()]

    def stock_report(self):
        s = "Current Stock:"
        for i in range(len(self.key_list)):
            s += f"\n{(i + 1):4d}. {str(self.key_list[i]):60} {self.stock.get(self.key_list[i]):6d}"
        return s

    def inbound(self, item, quantity):
        self.stock.update({item: self.stock.setdefault(item, 0) + int(quantity)})

    def outbound(self, item, quantity, location="write-off"):
        if self.stock.get(item) < int(quantity):
            return "Inventory transfer failed: not enough quantity in stock"
        self.stock.update({item: self.stock.get(item) - int(quantity)})
        return f"Inventory transfer {quantity} PCE from {__class__.__name__} to {location}: OK"


class OfficeEquipment(ABC):

    @abstractmethod
    def __init__(self, model):
        self.model = model


class Printer(OfficeEquipment):

    def __init__(self, model, kind, color):
        OfficeEquipment.__init__(self, model)
        self.kind = kind
        self.color = color

    def __str__(self):
        return f"{__class__.__name__}: {self.model}; Type: {self.kind}; {'Color' if self.color else 'Monochrome'}"


class Scanner(OfficeEquipment):
    def __init__(self, model, resolution, dummy=""):
        OfficeEquipment.__init__(self, model)
        self.resolution = resolution

    def __str__(self):
        return f"{__class__.__name__}: {self.model}; Resolution: {self.resolution} dpi"


class Copier(OfficeEquipment):
    def __init__(self, model, resolution, color):
        OfficeEquipment.__init__(self, model)
        self.resolution = resolution
        self.color = color

    def __str__(self):
        return f"{__class__.__name__}: {self.model}; Resolution: {self.resolution} dpi; " \
               f"{'Color' if self.color else 'Monochrome'}"


# main
w = Warehouse()
w.inbound(Printer("HP M15", "laser", False), 4)
w.inbound(Scanner("Canon L400", 4800), 10)
w.inbound(Copier("Xerox 302", 1200, False), 2)

while True:
    print("""
    \nMENU
    \tp\tPrint current stock
    \ti\tInbound delivery
    \to\tOutbound delivery
    \tq\tQuit
    """)
    inp = input("> ")
    if inp.upper() == 'Q':
        break

    if inp.upper() == 'P':
        print(w.stock_report())

    elif inp.upper() == 'O':  # inventory transfer from warehouse
        print(w.stock_report())
        inp = input("Outbound Delivery\nChoose item No. (other: main menu) ")
        if inp not in [str(el) for el in range(1, len(w.key_list) + 1)]:
            continue
        to_location = input("Move to: ")
        qty = input("Quantity: ")
        try:
            if not qty.isdigit() or (qty := int(qty)) < 1:
                raise MyException("Quantity should be a positive integer")
            print(w.outbound(w.key_list[int(inp) - 1], qty, to_location))
        except MyException as e:
            print(e)

    elif inp.upper() == 'I':  # coming of existing or new items
        print(w.stock_report())
        print(f"{'n':>4}. New item")
        inp = input("Inbound Delivery\nChoose item No. (n for new one, other: main menu) ")

        # # # NEW ASSORTMENT ITEM: BEGIN # # #
        if inp.upper() == 'N':
            item_model = input("Model (empty for main menu): ")
            if not item_model:
                continue
            item_type = input("Choose item type (1: printer; 2: scanner; 3: copier; other: main menu) ")
            if item_type == '1':
                item_class = Printer
                arg1 = input("Printer type (laser, jet, etc.) ")
                arg2 = True if input("Is it color (Y/N)? ").upper() == 'Y' else False
            elif item_type == '2':
                item_class = Scanner
                arg1 = input("Resolution, dpi: ")
                arg2 = ""
            elif item_type == '3':
                item_class = Copier
                arg1 = input("Resolution, dpi: ")
                arg2 = True if input("Is it color (Y/N)? ").upper() == 'Y' else False
            else:
                continue
            qty = input("Quantity: ")
            try:
                if not qty.isdigit() or (qty := int(qty)) < 1:
                    raise MyException("Quantity should be a positive integer")
                w.inbound(item_class(item_model, arg1, arg2), qty)
            except MyException as e:
                print(e)
        # # # NEW ASSORTMENT ITEM: END # # #

        elif inp in [str(el) for el in range(1, len(w.key_list) + 1)]:
            qty = input("Quantity: ")
            try:
                if not qty.isdigit() or (qty := int(qty)) < 1:
                    raise MyException("Quantity should be a positive integer")
                w.inbound(w.key_list[int(inp) - 1], qty)
            except MyException as e:
                print(e)
        else:
            continue

    input("\nPress Enter to return to menu")
