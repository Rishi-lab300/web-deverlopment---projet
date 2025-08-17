from random import randint
class Train:
    def __init__(self , trainNo):
        self.trainNo = trainNo
    def book(self, fro , to):
        print(f"Tickets is booked in the train no:  {self.trainNo} from {fro} to {to}")
    def getstatus(self):
        print(f"Tickets is booked in the train no:  {self.trainNo} is running in time")
    def getfare(self , fro , to):
        print(f"Ticket fare in the train no:  {self.trainNo} from {fro} to {to} is {randint(2345,5555)}")
       
       
t = Train(343434)
t.book("mumbai" , "Surat")  
t.getstatus()  
t.getfare("mumbai" , "Surat")    