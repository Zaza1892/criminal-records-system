import socket 

host = 'localhost'
port = 1024

def post_request(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.send(request.encode())
        response = sock.recv(1025).decode()
        print(response)

def profileSrch():
    name = input("Enter a name: ")
    request = f"searchName|{name}"
    post_request(request)

def crime_search():
    crime_committed = input("Insert Crime description: ")
    request = f"searchforcrime|{crime_committed}"
    post_request(request)

while True:
    print("[1] Search for a profile")
    print("[2] Search Criminal Record")
    print("[3] Exit")

    choice = input("Make your choice: ")

    if choice == "1":
        profileSrch()
    elif choice == "2":
        crime_search()
    elif choice == "3":
        break
    else:
        print("Choose another option")