class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

        print("Insert dollars/coins")

        dollars = int(input("How many dollars?: "))
        quarters = int(input("How many quarters?: "))
        halfDollar = int(input("How many half dollars?: "))
        nickels = int(input("How many nickels?: "))

        total = dollars + quarters * 0.25 + halfDollar * 0.50 + nickels * 0.05
        txt = f"Total: {total}"
        print(txt)

        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False

        change = coins - cost

        if change > 0:
            txt = (f"Here is ${change} in change.")
            print(txt)
        return True
