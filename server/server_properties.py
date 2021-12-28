def main():
    server_name = input("What is the server name: ")
    server_name.strip()
    ip = input("What is the ip address: ")
    ip.strip()
    netmask = input("What is the netmask: ")
    netmask.strip()

    print(server_name, ip, netmask, sep=",")

    print("servername: " + server_name)
    print("ip: " + ip)
    print("netmask: " + netmask)


main()

