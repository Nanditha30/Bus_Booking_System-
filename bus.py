import random
import enum
import calendar
import itertools
class route:
    def __init__(self,routeno,source,destination,price):
        self.routeno=routeno
        self.source=source
        self.destination=destination
        self.price=price
    def display(self):
        print("{0} : {1} to {2}".format(self.routeno,self.source,self.destination))

# Using enum class create enumerations
class BusType(enum.Enum):
   AC = 1
   NonAC = 2
   Sleeper = 3

class bus:
    listofavailseats=[]
    def __init__(self,name,categoryfee,lroutes,typb,luxuryfee,totalseats):
        self.name=name
        self.categoryfee=categoryfee
        self.lroutes=lroutes
        self.typb=typb
        self.luxuryfee=luxuryfee
        self.totalseats=totalseats
        self.availseats=totalseats
        self.column=['A','B','C','D']
        self.row=[str(i) for i in range(1,int(self.totalseats/4)+1)]
        test_list=list(itertools.product(self.row,self.column))
        res = list(map("".join, test_list))
        self.listofavailseats=[str(i)for i in res]
    def getseatno(self,seats):
        print(self.listofavailseats)
        f=[]
        for i in range(seats):
            l=input("enter the required seatno")
            p=self.listofavailseats.index(l)
            g=self.listofavailseats.pop(p)
            f.append(g)
        print(self.listofavailseats)
        self.availseats-=seats
        return f
class price:
    def __init__(self,bus,route):
        self.bus=bus
        self.route=route
    def getPrice(self):
        return self.route.price + self.bus.categoryfee +  self.bus.luxuryfee

class Reservation:
    def __init__(self, reservationId, bus, seats, above5, doj,seatnos):
        self.reservationId = reservationId
        self.seats = seats
        self.above5 = above5
        self.doj = doj
        self.seatnos=seatnos
    def display(self):
        print("--------Reservation---------")
        print("ReservationId = {0}".format(self.reservationId))
        print("Seats = {0}".format(self.seats))
        print("Your selected seat nos={0}".format(self.seatnos))
        print("Passengers Above 5 years = {0}".format(self.above5))
        print("Date of Journey = {0}".format(self.doj))
    def findDay(self):
        day, month, year = (int(i) for i in self.doj.split(' '))
        dayNumber = calendar.weekday(year, month, day)
        days =["Monday", "Tuesday", "Wednesday", "Thursday",
                         "Friday", "Saturday", "Sunday"]
        return (days[dayNumber])
    def generation_of_receipt(self,Busprice,day):
        self.Busprice=Busprice
        self.day=day
        print('original busprice={0}'.format(self.Busprice))
        if(self.day=="Sunday"):
            self.Busprice+=self.Busprice/10
            print("as the date of journey is sunday ,we charge 10% extra on the bus price")
        print('finalbusprice= {0}'.format(self.Busprice))
        total_amount=self.Busprice*self.seats
        print("Total amount={0}".format(total_amount))
        debitcardno=int(input("enter debit card no:"))
        amount=int(input("enter amount"))
        cvv=int(input("enter cvv"))
        print("*****receipt*******")
        print("no of seats={0}".format(self.seats))
        print("Total amount paid={0}".format(amount))
        if(total_amount-amount==0):
            print("you tickets is/are confirmed")
        else:
            print("amount insufficient")
r1=route(12,"lingampally","gachibowli",150)
r2=route(13,"lingampally","nanagramguda",200)
r3=route(14,"lingampally","gandipet",350)
r4=route(15,"gachibowli","nanagramguda",100)
r5=route(16,"gachibowli","kokapet",200)
r6=route(17,"lingampally","kokapet",500)
r7=route(18,"nanagramguda","gandipet",150)
r8=route(19,"nanagramguda","kokapet",100)
r9=route(20,"gachibowli","gandipet",200)
bAc = bus(1,100,[r1, r2, r3, r4, r7, r9], BusType.AC, 250,52)
bNAc = bus(2,100,[r1, r2, r3, r4, r7, r9], BusType.NonAC, 150,60)
bsl = bus(3,100,[r1, r2, r3, r4, r7, r9], BusType.Sleeper, 50,72)
b1Ac = bus(4,200,[r1, r2, r3, r4, r7, r9], BusType.AC, 250,56)
b1NAc = bus(5,200,[r1, r2, r3, r4, r7, r9], BusType.NonAC, 150,60)
b1sl = bus(6,200,[r1, r2, r3, r4, r7, r9], BusType.Sleeper, 50,72)

b2Ac = bus(7,100,[r1, r2, r6, r4, r5, r8], BusType.AC, 250,48)
b2NAc = bus(8,100,[r1, r2, r6, r4, r5, r8], BusType.NonAC, 150,60)
b2sl = bus(9,100,[r1, r2, r6, r4, r5, r8], BusType.Sleeper, 52,72)
b3Ac = bus(10,200,[r1, r2, r6, r4, r5, r8], BusType.AC, 250,60)
b3NAc = bus(11,200,[r1, r2, r6, r4, r5, r8], BusType.NonAC, 150,56)
b3sl = bus(12,200,[r1, r2, r6, r4, r5, r8], BusType.Sleeper, 50,76)
Buses = [bAc, bNAc, bsl, b1Ac, b1NAc, b1sl, b2Ac, b2NAc, b2sl, b3Ac, b3NAc, b3sl]

ch="y"
while(ch=="y"):
    print("***********NANDITHA TRAVELS**************")
    for r in [r1,r2,r3,r4,r5,r6,r7,r8,r9]:
        r.display()
    start=input("enter the starting point from the given chart")
    end=input("enter the end point from the given chart")
    reqroute=int(input("enter the choose routeno"))

    for b in Buses:
        for r in b.lroutes:
           if (reqroute==r.routeno):
               p=price(b, r)
               busprice = p.getPrice()
               print(" Bus Number ={0}, Price ={1}, No of seats in bus:{2}, BusType ={3}".format(b.name,busprice,b.availseats,b.typb.name))

    busChoosen=int(input("Choose the Bus Number:"))
    above5=input("Number of passengers above 5 years of age:")
    seats=int(input("Provide number of seats:"))
    doj=input("Enter Date of journey in the format dd mm yyyy:")
    k=busChoosen-1
    b=Buses[k]
    seatnos=b.getseatno(seats)
    for r in b.lroutes:
        if (reqroute==r.routeno):
             p=price(b,r)
             busprice=p.getPrice()
    reservation = Reservation(random.randint(1736, 1895), busChoosen, seats, above5, doj,seatnos)
    day=reservation.findDay()
    reservation.display()
    reservation.generation_of_receipt(busprice,day)


    ch=input("do u want to continuey/n")
