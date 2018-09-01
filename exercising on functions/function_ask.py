def ask(message, options):
    while True:
        response = input("{0} [{1}]: ".format(message, "/".join(options)))
        possible_options = set(option for idx in range(1, len(response)+1)
            for option in options if response[:idx] == option[:idx])
        if len(possible_options) == 1:
            return list(possible_options)[0]
        else:
            print("Unknown option: {0}, try again".format(response))

def ask_yes_no(message):
    return (ask(message, ["yes", "no"]) == "yes")

def get_order(person):
    sugar_question = "Person {0}, Would you like Sugar?".format(person)
    if ask_yes_no(sugar_question):
        sugar = int(input("How many sugars? "))
    else:
        print("Okay, No sugar")
        sugar = None

    milk = ask("How Much Milk Would You Like?", ["small", "medium", "large"])
    print("Order is being processed, next order:\n")
    return {"person": person, "sugar": sugar, "milk": milk}

def process_orders():
    while 1:
        print("Making A Cup Of Tea")
        num_orders = int(input("How many for Tea? "))
        print("There are {0} people for tea".format(num_orders))

        orders = [get_order(person) for person in range(1, num_orders+1)]
        print('The orders has been processed with these data:')
        for order in orders:
            print(" ".join([
                ' - Person {0} wants tea'.format(order["person"]),
                ('with {0}'.format(order['sugar']) if order['sugar'] else 'without'), 
                "sugar and {0} milk".format(order["milk"]),
            ])

        if not ask_yes_no('Would you like to re-order?'):
            print("\nOkay, Thank You, Enjoy Your Tea")
            break

process_orders()
