def contactBook():

    with open("contacts.txt", "a") as file:
        while True:
            enter = input("add[a], remove[-a], search[s], quit[x]: ")
            if enter.lower() == 'a':
                fname=input("Enter First Name: ")
                lname=input("Enter Last Name: ")
                email = input("Enter E-mail: ")
                phone = str(input("Enter Phone No. : "))
                address = input("Enter Address: ")
                info = fname.capitalize() +" "+ lname.capitalize() + ":" + phone + " Address: " + address + " E-mail: " + email + "\n"
                file.writelines(info)

            elif enter.lower() == "-a":
                with open("contacts.txt", 'r') as file:
                    removing = input("Enter Person's Name: ")
                    for info in file.readlines():
                        if removing in info:
                             removing.replace(removing ,"Removed")       
                             print(removing)
                    if not removing in info:
                        print("400")

            elif enter.lower() == 's':
                with open("contacts.txt", 'r') as file:
                    search = input("Search: ")
                    flag = False
                    for info in file.readlines():
                        if search in info:
                            print(info)
                            flag = True
                    if not flag:
                        print("404")

            else:
                print("Dear User! Enter the valid entry. Thank You !")

            if enter.lower() == 'x':
                print("Thanks for checking in !")
                break

contactBook()


