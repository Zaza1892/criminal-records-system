import socket 

host = 'localhost'
port = 1024

def post_request(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.send(request.encode())
        response = sock.recv(1025).decode()
        print(response)

def adminlogin():
    username = input("Enter username:")
    password = input("Enter password:")
    request = f"adminlogin|{username}|{password}"
    post_request(request)

def new_profile():
    id = input("Enter ID:")
    name = input("Enter Name:")
    surname = input("Enter surname:")
    cell = input("Enter cell:")
    email = input("enter email:")
    unit_num = input("Enter unit number: ")
    estate_name = input("Enter estate name: ")
    street_name = input("Enter street name:")
    suburb = input("Enter suburb:")
    town = input("Enter town:")
    
    new_profile = f"id={id}&name={name}&surname={surname}&cell={cell}&email={email}&unit_num={unit_num}&estate_name={estate_name}&street_name={street_name}&suburb={suburb}&town={town}"
    request = f"profileadd|{new_profile}"
    post_request(request)

def newCriminal():
    crime_id = input("Enter crime id:")
    description = input("Enter Description:")
    date = input("Enter date :")
    severity_level = input("Enter severity Level:")
    person_id = input("Enter person id:")
    log_date = input("Enter log date:")
    
    add_entries = f"crime_id={crime_id}&description={description}&date={date}&severity_level={severity_level}&person_id={person_id}&log_date={log_date}"
    request = f"newCriminal|{add_entries}"
    post_request(request)

def profileSrch():
    name = input("Enter name:")
    request = f"searchName|{name}"
    post_request(request)

def crime_search():
    crime_committed = input("Insert Crime description: ")
    request = f"searchforcrime|{crime_committed}"
    post_request(request)

while True:
    print("[1] Search for profile")
    print("[2] Search Criminal Record")
    print("[3] Add profile")
    print("[4] Add criminal")
    print("[5] Exit")

    choice = input("Make your choice:")

    if choice == "1":
        profileSrch()
    elif choice == "2":
        crime_search()
    elif choice == "3":
        new_profile()
    elif choice == "4":
        newCriminal()
    elif choice == "5":
        break