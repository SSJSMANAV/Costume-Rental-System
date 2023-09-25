import datetime
import random

#This function open the txt file and read and kept it in a list
def file_stock():
    file = open("stock.txt","r")
    data = file.readlines()
    file.close()
    return data

#This function put the file in an empty dictionar
data = {}
def dictionary_data(file_content):
    for index in range(len(file_content)):
        data[index+1] = file_content[index].replace("\n","").split(",")
    #print(data)
    return data

#This function print the dictionary in a tabular formate
def printcostume():
    file_content = file_stock()
    main_data = dictionary_data(file_content)
    print("-"*105)
    print("ID","\t","Costume Name","\t","Brand","\t\t","Price","\t","Quantity")
    print("-"*105)
    for key,value in main_data.items():
        print(key,"\t",value[0],"\t",value[1],"\t",value[2],"\t",value[3])
    print("-"*105)
    return main_data
    

#This function check validation of costume ID
def logical_Id():
    file_content = file_stock()
    main_data = dictionary_data(file_content)

    valid_data = False

    while  valid_data == False:
        printcostume()
        while True:
            try:
                ID = int(input("\n Enter the ID of the costume you want: "))
                break
            except:
                print("")
                print("Invalid Input!!!\nSelect the given ID of the costumes")
                print("")
        if ID > 0 and ID <= 7:
            valid_data = True
            return ID
        else:
            print("*"*45)
            print("\tPlease provide a valid costume ID !!!")
            print("*"*45,"\n")


costume_Name = []
price_total = []
brand1 = []

def logical_quantity(ID):
    file_content = file_stock()
    main_data = dictionary_data(file_content)
    while True:
        try:
            print("")
            quantity_1 = int(input("Enter the number of quantity: "))
            break
        except:
            print("")
            print("Invalid Input!!!\nSelect the quantity which are in stock")
            print("")
    if 0 < quantity_1 <= int(main_data[ID][3]):
        main_data[ID][3] = str(int(main_data[ID][3])-quantity_1)
        print(main_data)
        file = open("stock.txt","w")
        for key,value in data.items():
            string = ",".join(value)
            file.write(string)
            file.write("\n")
        file.close()
        C_name = main_data[ID][0]
        brand = main_data[ID][1]
        price = main_data[ID][2]
        total_price = float(main_data[ID][2].replace("$","")) * quantity_1
        qty = quantity_1
        price_total.append(total_price)
        costume_Name.append(C_name)
        brand1.append(brand)
        print("")
        ask = input("Do you want to rent more costume? (yes/no)").lower()
        print("")
        if ask == "yes":
            renting_costume()
        else:
             invoice()
    elif quantity_1 > int(main_data[ID][3]):
        print("")
        print("*"*70)
        print("\tSorry we don't have that much quantity in stock!!!")
        print("*"*70)
    elif quantity_1 <= 0:
        print("\n","*"*30)
        print("\tInvalid Input")
        print("*"*30)
    return quantity_1

def renting_costume():
    file_content = file_stock()
    main_data = dictionary_data(file_content)
    ID = logical_Id()
    quantity_1 = logical_quantity(ID)
    

billinvoice = []
#This function generate bill.
def invoice():
    print("")
    name = (input("Enter Customer Name: "))
    phone = (input("Enter Customer Phone Number: "))
    x = datetime.datetime.now()
    a = x.strftime('%Y-%m-%d %A')
    print("")
    print("*"*53)
    print("\t\tRent Bill Details")
    print("*"*53)
    print("Name of Customer: ",name)
    print("Phone Number of Customer: ",phone)
    print("Date of rent: ",a)
    print("-"*58)
    print("Costume Name: ", costume_Name)#,C_name)
    print("Brand: ", brand1)#,brand)
    print("Total Amount: $", total())#,total_price)
    print("-"*58)

    rent_bill = "---------------Rent Bill----------------------"
    product_details = "-----------Costume Details-------------------"
    blank = "-----------------------------------------------"
    frandom = random.randint(1,100)
    varfile = name+str(frandom)+".txt"
    
    billinvoice.append(rent_bill)
    billinvoice.append("\nCustomer Name: "+name)
    billinvoice.append("Customer Phone Number: "+phone)
    billinvoice.append("Date Of Rent: "+a+"\n" )
    billinvoice.append(product_details)
    billinvoice.append("\nCostume Name: "+str(costume_Name))
    billinvoice.append("Brand Name: "+str(brand1))
    billinvoice.append("Total Amount: $"+str(total())+"\n")
    billinvoice.append(blank)
    file = open(varfile,"w")
    for i in billinvoice:
        file.write(f"{i}\n")
    file.close


dic = []
def total():
    s = 0
    for k in range(len(price_total)):
        dic = price_total[k]
        s += dic
    return s


    
    














    
        









