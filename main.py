def profit_calc():
    # input
    hours_worked = float(input("Hours: "))
    pay_per_hour = float(input("Pay per hour: "))

    # Calculation of total accruals
    total_earnings = hours_worked * pay_per_hour

    # Calculation of military tax
    military_tax = 0.015 * total_earnings

    # Calculation of taxes and social contributions
    tax_and_social_contributions = 0.18 * total_earnings

    # Calculation of clear profit
    net_earnings = total_earnings - military_tax - tax_and_social_contributions

    # output
    print("Total earn: ", total_earnings)
    print("Military tax (1.5%): ", military_tax)
    print("Calculation of taxes and social contributions (18%): ", tax_and_social_contributions)
    print("Clear profit: ", net_earnings)

def check_robinson_rights():
    # input
    a = float(input("Enter the length of the island side in metres: "))
    n = int(input("Enter the number of Robinsons: "))
    # island area
    island_area = a ** 2
    # one robinson area
    robinson_area = island_area / n
    
    # Checking whether Robinson's rights to living space have been violated
    if robinson_area >= 1:
        print("Robinson's rights to living space have not been violated.")
        # Calculating the number of Robinsons that can still be accommodated
        add_robinsons = int(island_area // robinson_area) - n
        print("It is possible to move %s more Robinsons to island without violating their right to the area." % (add_robinsons)
    else:
        print("Robinson's rights to living space violated.")


def main():
    print("What program do you want to use?")
    print("(P)rofit with taxes")
    print("(R)obinsons rights")
    x = input("> ")
    if x=="P" or x=="p":
      profit_calc()
    elif x=="R" or x=="r":
      check_robinson_rights()
   else:
      print("Err: invalid input")

main()
