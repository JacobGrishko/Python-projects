import threading
import os


# manage adding new clients
def worker(server, clients):
    while True:
        client, addr = server.accept()
        clients.append([client, addr])


# print client list
def print_clients(clients):
    counter = 0
    print("------------ Clients ------------")
    for client in clients:
        print("{0} = {1}".format(counter, client[1][0]))
        counter+=1
    print("---------------------------------")



# find self ip
def get_ip():
    ip = os.popen("ipconfig")
    for line in ip.readlines():
        if "IPv4 Address" in line:
            start = line.find(":")
            end = -1
            output = line[start+2:end]
            break
    return output


# ping an ip
def scanner(ip_address, client_list, lock):
    result = os.popen("ping {0} -n 1".format(ip_address)).read()

    if "TTL" in result:
        with lock:
            print(ip_address)
            client_list.append(ip_address)


#scan network
def scan_net():
    my_ip = get_ip()
    network = my_ip[:my_ip.rfind(".")]
    client_list = []
    threads = []
    lock = threading.Lock()

    for item in range(1, 255):
        test = network + str(item)
        t = threading.Thread(target=scanner, args=(test, client_list, lock,))
        t.start()
    print("connected to you:")
    print(client_list)



def send_comm(clients):

    if clients:
        print("Choose a client or Choose 0 for all clients")
        print_clients(clients)
        selected_client = input("> ")
        command = input("Command:")
        if selected_client == "all":
            for client in clients:
                try:
                    client.sendall(command.encode())
                    result = client.recv(2048).decode()
                    print(result)
                except:
                    clients.remove(client)
        else:
            client_socket = clients[int(selected_client)][0]

            client_socket.sendall(command.encode())
            result = client_socket.recv(2048).decode()
            print(result)
    else:
        print("There are no clients")

