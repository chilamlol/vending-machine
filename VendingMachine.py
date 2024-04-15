class VendingMachine:
    def __init__(self):
        self.drinks = {
            "100 Plus": 2,
            "Coca Cola": 2,
            "Pepsi Cola": 2,
            "Mineral Water": 1,
            "Honey Lemon": 5
        }

    def purchase(self, received, price):
        notes = [50, 20, 10, 5, 1]
        change = {}
        for note in notes:
            numNotes = (received - price) // note
            if numNotes:
                change[note] = numNotes
                received -= numNotes * note
        return change

    def menu(self):
        for drink, price in self.drinks.items():
            print(drink, " : RM", price)

def main():
    vendingMachine = VendingMachine()
    vendingMachine.menu()
    print("type 'quit' to exit")

    while True:
        selection = input("\nPlease select a drink: ").title()
        # quit to break the loop
        if selection.lower() == "quit":
            print("Exited")
            break

        # Invalid option entered
        if selection not in vendingMachine.drinks:
            print("Sorry, we don't sell this item")
            continue

        received = int(input("Please insert note: "))
        # Invalid note entered
        if received not in [100, 50, 20, 5, 1]:
            print("Invalid note entered")
            continue

        price = vendingMachine.drinks[selection]
        # Insufficient amount
        if received < price:
            print("Not enough money")
            continue

        change = vendingMachine.purchase(received, price)

        if change:
            print("Changes: ")
            for note, amount in change.items():
                print(amount, "* RM", note)
        print(selection, "dispensed, thank you")


if __name__ == "__main__":
    main()