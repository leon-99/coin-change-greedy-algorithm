def main():
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = round(cents - quarters * 0.25, 2)

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = round(cents - dimes * 0.10, 2)

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = round(cents - nickels * 0.05, 2)

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = round(cents - pennies * 0.01, 2)
    
    print_results(quarters, dimes, nickels, pennies)


def get_cents():
    while True:
        try:
            n = float(input("Changed owed: "))
            break
        except ValueError:
            print("Please enter valid change example: 1.00")
            continue
    return n


def calculate_quarters(cents):
    n = 0
    while cents >= 0.25:
        n += 1
        cents = round(cents - 0.25, 2)
    return n


def calculate_dimes(cents):
    n = 0
    while cents >= 0.10:
        n += 1
        cents = round(cents - 0.10, 2)
    return n


def calculate_nickels(cents):
    n = 0
    while cents >= 0.05:
        n += 1
        cents = round(cents - 0.05, 2)
    return n


def calculate_pennies(cents):
    n = 0
    while cents >= 0.01:
        n += 1
        cents = round(cents - 0.01, 2)
    return n


def print_results(quarters, dimes, nickels, pennies):
    coins = quarters + dimes + nickels + pennies
    print()
    print(f"quarters: {quarters}", f"dimes: {dimes}", f"nickels {nickels}", f"pennies {pennies}", f"total of {coins} coins", sep="\n")

main()
