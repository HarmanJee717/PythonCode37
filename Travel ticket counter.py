passenger_name = input("Enter your name: ")
destination = input("Enter your destination: ")
ticket_price = float(input("Enter ticket price: "))
number_of_tickets = int(input("Enter number of tickets: "))

total = ticket_price * number_of_tickets

print("Passenger:", passenger_name)
print("Destination:", destination)
print("Total price:", total)

if destination == "India":
    print("Have a great trip!")

if destination == "USA":
    print("if possible Cancel the trip, Trump is Crazy!")

if number_of_tickets > 1:
    print("Booking is confirmed! ",passenger_name)
    print("Plane will come in around 4-5 hours!")