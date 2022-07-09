x = 1044
y = "close"
z = "open"
q = "quit"

while True:
    password = int(input("Enter Password: "))
    command = (input("Enter Command: "))

    if password == x:

        print("Login Successful!")

    else:
        print("Wrong Password")

    if command == y:
        print("The door is locked")
        break

    if command == z:
        print("The door is open!")
        break

    if len(command) != len(set(command)):
        print("The door is already open")
        break

    if command == q:
        print("Process terminated")
        break

    print("Invalid Input")
import datetime

e = datetime.datetime.now()

print("The door was last opened at = %s" % e)
