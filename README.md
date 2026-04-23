# criminal-records-system
Developed as part of my academic studies as a final-year project


This project demonstrates:
- Client-server communication using Python sockets
- Multi-threaded server handling multiple clients
- Separate admin and normal user clients
- SQL database design for storing criminal records

---

##  Technologies Used

- Python (Sockets, Threading)
- Microsoft SQL Server (Database Design)
- SQL (DDL & DML)

---

##  System Structure

###  Server
- Handles incoming client requests
- Processes commands such as:
  - Add profile
  - Add criminal record
  - Search profile
  - Search crime

###  Admin Client
- Login functionality
- Add new profiles
- Add criminal records
- Search data

###  Normal Client
- Search profiles
- Search criminal records



###  Database
Contains 3 tables:
- Profile_table
- Crime_table
- Admin_table

