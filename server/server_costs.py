

def main():
    price_vps = float(input("What is price per month for one VPS?: "))
    amount_vps = int(input("How many VPS servers do you need?: "))
    provision_time = int(input("How many minutes needs an administrator to provision one VPS?: "))

    total_cost = str(price_vps*amount_vps*provision_time)
    final = "The total cost for " + str(amount_vps) + " servers is " + total_cost + "euro "
    print(final)


main()

