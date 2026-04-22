import threading
import socket

host = 'localhost'
port = 1024

def client_req(client_socket):
    while True:
        client_Sent = client_socket.recv(1024).decode()
        if not client_Sent:
            break

        response = process_response(client_Sent)
        client_socket.send(response.encode())

    client_socket.close()

def process_response(request):
    parts = request.split('|', 1)
    choice = parts[0]
    dtbs = parts[1] if len(parts) > 1 else ""

    if choice == "adminlogin":
        username, password = dtbs.split('|')
        response = f"Admin Login: username={username}, password={password}"

    elif choice == "profileadd":
        new_profile = dtbs
        response = f"New Profile added: {new_profile}"

    elif choice == "newCriminal":
        newCriminal = dtbs
        response = f"New Criminal added: {newCriminal}"

    elif choice == "searchName":
        name = dtbs
        response = f"Enter name: {name}"

    elif choice == "searchforcrime":
        crime_comitted = dtbs
        response = f"Insert crime description {crime_comitted}"

    else:
        response = "Choose another option"

    return response

def server_start():
    serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverS.bind((host, port))
    serverS.listen(10)

    print("Listening for connections")

    while True:
        client_socket, client_address = serverS.accept()
        print(f"Connection from {client_address[0]}:{client_address[1]}")

        client_thread = threading.Thread(target=client_req, args=(client_socket,))
        client_thread.start()

server_start()