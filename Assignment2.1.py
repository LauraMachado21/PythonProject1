def Order():
    StrawberryTwizzler=0
    ChocolateDip=0
    VanillaChai=0
    HoneyDrizzled=0

    while True:
        OrderChoice=(raw_input("Select your doughnut.\n1. Strawberry Twizzler\n2. Chocolate Dipped Maple Puff\n" \
        "3. Vanilla Chai Strudel\n4. Honey Drizzled Lemon Dutchie\n5.Done\n"))

        while OrderChoice.isdigit()==False:
            print "Error: %s is not a valid option.\n" % OrderChoice
            OrderChoice=(raw_input("Select your doughnut.\n1. Strawberry Twizzler\n2. Chocolate Dipped Maple Puff\n" \
            "3. Vanilla Chai Strudel\n4. Honey Drizzled Lemon Dutchie\n5.Done\n"))

        OrderChoice=int(OrderChoice)

        while OrderChoice < 1 or OrderChoice > 5:
            print "Error: %s is not a valid option.\n" % OrderChoice
            OrderChoice=int(raw_input("Select your doughnut.\n1. Strawberry Twizzler\n2. Chocolate Dipped Maple Puff\n" \
                "3. Vanilla Chai Strudel\n4. Honey Drizzled Lemon Dutchie\n5.Done\n"))

        if OrderChoice == 5:
            break

        else:
            PurchaseNumber=(raw_input("How many would you like? "))

            while PurchaseNumber.isdigit() == False:
                PurchaseNumber=raw_input("How many would you like? ")

            PurchaseNumber=int(PurchaseNumber)
            if OrderChoice == 1 : StrawberryTwizzler += PurchaseNumber
            if OrderChoice == 2 : ChocolateDip += PurchaseNumber
            if OrderChoice == 3 : VanillaChai += PurchaseNumber
            if OrderChoice == 4 : HoneyDrizzled += PurchaseNumber

    return (StrawberryTwizzler,ChocolateDip,VanillaChai,HoneyDrizzled)

def checkOut(d1,d2,d3,d4):

    total = 0.00
    Confirmation = 'n'

    print "Your order:"
    print "%s Strawberry Twizzlers\n" % (d1)
    print "%s Chocolate Dipped Maple Puffs\n" % (d2)
    print "%s Vanilla Chai Strudels\n" % (d3)
    print "%s Honet Drizzled Lemon Dutchies\n" % (d4)

    Confirmation = raw_input("Confirm? (y/n)")
    total=(d1*2.00)+(d2*3.25)+(d3*2.75)+(d4*2.50)

    if Confirmation == 'y':
        print"Your total comes to: $%.2f" % round(total,2)
        if total !=0:
            print "Thanks for your order!"
        return mainMenu()
    else:
        return mainMenu()

def mainMenu():

    d1=0
    d2=0
    d3=0
    d4=0

    while True:
        menuChoice=(raw_input ("Welcome to Dino's Doughnut Shoppe.\n"\
            "1. Order\n2. Check Out\n3. Start Over.\n4. Exit\n"))

        while menuChoice.isdigit()==False:
            print "Error: %s is an invalid option\n" % (menuChoice)
            menuChoice=(raw_input ("Welcome to Dino's Doughnut Shoppe.\n"\
                "1. Order\n2. Check Out\n3. Start Over.\n4. Exit\n"))

        menuChoice = int(menuChoice)

        while menuChoice < 1 or menuChoice > 4:
            print "Error: %s is an invalid option\n" % (menuChoice)
            menuChoice=(raw_input ("Welcome to Dino's Doughnut Shoppe.\n"\
                    "1. Order\n2. Check Out\n3. Start Over.\n4. Exit\n"))
        if menuChoice == 4:
            return 0

        if menuChoice == 3 : mainMenu ()
        if menuChoice == 2 : return checkOut(d1,d2,d3,d4)
        if menuChoice == 1 :

            Purchase1,Purchase2,Purchase3,Purchase4=Order()
            d1=d1+Purchase1
            d2=d2+Purchase2
            d3=d3+Purchase3
            d4=d4+Purchase4



mainMenu()
print "Goodbye!"
