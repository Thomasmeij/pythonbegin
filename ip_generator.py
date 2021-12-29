def ask_number(minimum=0, max_tries=3):

    for number in range(minimum, max_tries):
        number = int(input("Name a number: "))
        if number < minimum:
            return number, print("Niet kleiner dan 0 graag!")
        else:
            return number


def generate_ip_addresses(start_octet, end_octet, base="192.168.178"):
    '''implementeer
       sanitize eventueel start en end
       print de adressen 192.168.178.start t/m 192.168.178.end
    '''

    for ip_address in range(start_octet, end_octet):
        ip = f"{base}.{ip_address}"
        return ip

def main():
    print("Hoeveel ip-adressen moeten er worden gemaakt?")
    ip_count = ask_number()

    print("Wat is het start-octet?")
    ip_start = ask_number(minimum=0)
    ip_end = 255  # fixture, zelf bedenken!

    generate_ip_addresses(ip_start, ip_end)


if __name__ == "__main__":
    main()