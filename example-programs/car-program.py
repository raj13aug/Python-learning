command = ""
started = False
while command != "quit":
    command = input(">").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car is started")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car is stopped")

    elif command == "help":
        print("""
stop  - to stop the car
start - to start the car
quit  - to quit
            """)
    elif command == "quit":
         break
    else:
        print("sorry. I don't understand")


