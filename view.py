def view():
    print("\n\t\t\tLet's view costume.\n")

#This function open the txt file and read and kept it in a list
def file_stock():
    file = open("stock.txt","r")
    data = file.readlines()
    file.close()
    #print(data)
    return data

#This function put the file in an empty dictionar
def dictionary_data(file_content):
    data = {}
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
    


