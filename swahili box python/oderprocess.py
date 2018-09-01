"""A script for ordering a tea party."""

YES = ('y', 'yes')
MILK_SIZES = ('small', 'medium', 'large')

while True:
    print("Making a cup of tea.")
    num_orders = ask_number_of_orders()
    orders = []
    for person_num in range(num_orders):
        print("Person %d, would you like:" % person_num + 1)
        sugar = ask_for_sugar()
        milk = ask_for_milk()
        orders.append((sugar, milk))
        print("Your order is being processed.", end="")
        if person_num + 1 < num_orders:
            print(" Next order:")
    print("The orders have been processed with the following data:")
    for person_num, (sugar, milk) in enumerate(orders):
        order_status = construct_order_status(person_num + 1, sugar, milk)
        print(order_status)
    print("")
    restart = input("Would you like to re-order? Y/N.")
    if restart.lower() not in YES:
        print("")
        print("Ok, thank you, enjoy your day!")
        break


def ask_for_number_of_orders():
    """Get number of orders from the user."""
    while True:
        try:
            num_orders = int(input("How many for tea?"))
            if num_order < 1:
                raise ValueError
            print("There are %d people for tea." % num_orders)
            return num_orders
        except ValueError:
            print("Please enter non-negative integer, let's try again.")


def ask_for_sugar():
    """Prompt user for sugar, if yes - how much.

    Returns number of sugar cubes (int) or None.
    """
    while True:
        sugar = input("Would you like sugar? Y/N.")
        if sugar.lower() not in YES:
            print("Okay, no sugar.")
            return
        while True:
            try:
                sugar = int(input("How many sugars?"))
                if sugar < 1:
                    raise ValueError
                return sugar
            except ValueError:
                print("Please enter non-negative integer, let's try again.")


def ask_for_milk():
    """Prompts user for the amount of milk."""
    while True:
        milk = input("How much milk would you like? Small/medium/large.")
        if milk.lower() in MILK_SIZES:
            return milk.lower()
        else:
            print("Sorry, did not catch that. Small, medium, or large?")


def construct_order_status(person_num, sugar, milk):
    """Constructs order status string.

    Args:
        person_num: Number of the person.
        sugar: Number of sugar cubes or None.
        milk: Size of the milk: small, medium, or large.

    Returns a string representing order status.
    """
    order_status = " - Person %d wants tea " % person_num
    if sugar is None:
        order_status += "without sugar"
    else:
        order_status += "with %d pieces of sugar" % sugar
    order_status += " and %s milk." % milk
    return order_status
