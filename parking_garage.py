class ParkingGarage():
    currentTicket = {}
    availableTickets = ["ticket", "ticket", "ticket", "ticket", "ticket"]
    parkingSpaces = ["space", "space", "space", "space", "space"]


    def __init__(self):
        self.currentTicket["paid"] = False


    def takeTicket(self):
        # decrease the amount of tickets and parking spaces available by 1
        print("Please take a ticket and find an open space...")
        self.availableTickets.remove("ticket")
        self.parkingSpaces.remove("space")


    def payForParking(self):
        # display input for amount paid and check if they paid
        payment = input("Please enter 'pay' to complete your payment' ")
        if payment.lower() == "pay":
            print("Thanks! Your ticket has been paid, you have 15 minutes to leave. ")
            self.currentTicket["paid"] = True


    def leaveGarage(self):
        # if paid, thank them. If not, ask last time
        if self.currentTicket["paid"] == True:
            print("Thank you, have a nice day!")
        else:
            request = input("FINAL chance to make your payment  (enter 'pay')... ")
            if request.lower() == "pay":
                print("Thank you, have a nice day!")
                self.currentTicket["paid"] = True
            else:
                print("Quit trying to steal! Police are on the way!!")

        self.availableTickets.append("ticket")
        self.parkingSpaces.append("space")
        del self.currentTicket["paid"]


my_spot = ParkingGarage()

def run(spot):
    spot.takeTicket()
    spot.payForParking()
    spot.leaveGarage()

run(my_spot)