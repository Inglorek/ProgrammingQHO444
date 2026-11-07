def sum_weights(wc,wi):
    return wc + wi


def calc_avg_weight(wc, wi):
    total = sum_weights(wc, wi)
    return total / 2


def run():
    wc = float(input("What is the weight of the person?\n"))
    wi = float(input("What is the weight of their inventory?\n"))
    choice = input("What would you like to calculate (sum or average)?\n")

    if choice == "sum":
        print("The sum of weights is " + str(sum_weights(wc, wi)) + ".")
    elif choice == "average":
        print("The average weight is " + str(calc_avg_weight(wc, wi)) + ".")


run()