
class SandwichMaker:
    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for x in ingredients:
            if self.machine_resources[x] < ingredients[x]:
                print("Sorry, there is not enough" + x + ".")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

        for x in order_ingredients:
            self.machine_resources[x] -= order_ingredients[x]
        print("<" + sandwich_size + "> sandwich is ready. Bon appetit!")