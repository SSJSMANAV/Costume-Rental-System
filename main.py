import view
import rent
import return1

def main():
    print("+" * 50)
    print("\t\tWelcome to Costume Application")
    print("+" * 50)
    loop1 = False
    while loop1 == False:
        loop2 = True
        while loop2 == True:
            try:
                a = input("\nSelect the desirable option\
                              \n(1) || Select 1 to view the costumes.\
                              \n(2) || Select 2 to rent the costumes.\
                              \n(3) || Select 3 to return the costumes.\
                              \n(4) || Select 4 to exit the application.\
                              \nEnter the option: ")
                loop2 = False
            except:
                print("Invalid Input!!!")
            if a == "1":
                view.printcostume()
            elif a == "2":
                rent.renting_costume()
            elif a == "3":
                return1.returning_costume()
            elif a == "4":
                bye = input("\nDo you really want to quit?? (Yes/No): ").lower()
                if bye == "yes":
                    print("")
                    print("*"*49)
                    print("|\tThank you for shopping. Please visit again.\t|")
                    print("*"*49)
                    print("")
                    loop1 = True
            else:
                print("\n","*"*65)
                print("\tPlease select the value as per the provided option.")
                print(" ","*"*65)

main()


