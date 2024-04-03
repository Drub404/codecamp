import random


def discountCalculation():
    # Asking user input and storing in their variables used for later calculation
    full_price = int(input("How much does the article cost?: "))
    discount = int(input("How much % discount is there?: "))

    # Check if full_price variable is empty, if so assign it a random integer to calculate with
    if full_price == '':
        full_price = random.randint(1, 1000)
        print("That is not a valid input! Using random assigned values instead...")
        discount_amount = int(full_price) / 100 * int(discount)
        calculated_discount = int(full_price) - discount_amount
        print(f"You should've paid €{full_price}, but due to a discount of %{discount} the article now costs: {calculated_discount}")

    # Check if discount variable is empty, if so assign it a random integer to calculate with
    elif discount == '': # We have to check for an empty string, as
        discount = random.randint(1, 100)
        print("That is not a valid input! Using random assigned values instead...")
        discount_amount = int(full_price) / 100 * int(discount)
        calculated_discount = int(full_price) - discount_amount
        print(f"You should've paid €{full_price}, but due to a discount of %{discount} the article now costs: {calculated_discount}")

    # Serving as all the above criteria is met, the calculation will just take place with given inputs
    else:
        discount_amount = full_price / 100 * discount
        calculated_discount = full_price - discount_amount
        print(f"You should've paid €{full_price}, but due to a discount of %{discount} the article now costs: {calculated_discount}")


discountCalculation()
