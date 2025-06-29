import data
from sandwich_maker import SandwichMaker
from cashier import Cashier
import data, cashier, sandwich_maker


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()




def main():



    while True:
        menu = input("What would you like? (small/ medium/ large/ off/ report): ")

        if menu == "off":
            break
        elif menu == "report":
            for x, y in sandwich_maker_instance.machine_resources.items():
                if x == "cheese":
                    print(x + ": " + str(y) + " pound(s).")
                else:
                    print(x + ": " + str(y) + " slice(s).")
        elif menu in recipes:
            order = recipes[menu]
            if sandwich_maker_instance.check_resources(order["ingredients"]):
                pay = cashier_instance.process_coins()
                if cashier_instance.transaction_result(pay, order["cost"]):
                    sandwich_maker_instance.make_sandwich(menu, order["ingredients"])

if __name__=="__main__":
    main()
