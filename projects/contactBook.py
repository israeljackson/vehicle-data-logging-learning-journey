#introduction
print("☎️ Contact Book📗")

#create the dictionary
contact_book = {
    "Jackson" : {
        "Phone-number": '0708-692-8340\n',
        "E-mail": "Jacksonisrael2007@gmail.com\n",
        "Adress": "12, Ogunbekun street, Ladilak, Bariga, Lagos State\n"
    },

    "Samuel":{
        "Phone-number": '0703-267-8440\n',
        "E-mail": "akinleyesamuel37@gmail.com\n",
        "Adress": "15, Olubegon street, Onipanu, Bariga, Lagos State\n"
    },
     "Ezekiel":{
        "Phone-number": '0702-514-6309\n',
        "E-mail": "nwokologerald54@gmail.com\n",
        "Adress": "15, Adeyele street, Miyaki, Oworo-shoki, Lagos State\n"
    },
}

#display contacts
name = input("Enter contact name: ")
print(contact_book[name])

#add or delete conatcts
ans = input("Do you wish to modify contacts?(y/n) ")
ans = ans.lower()

while True:
    if ans == 'y':
        choice = input("Add(a), Delete(d) ")
        choice = choice.lower()
        
        #block to add new contact
        if choice == 'a':
           
            #prompt for new contact detail
            new_name = input("Enter contact name: ")
            new_number = input("Enter phone number: ")
            new_mail = input("Enter e-mail: ")
            new_adress = input("Enter adress: ")
            
            #create a dictionary for new_name inside the contact_book dictionary
            contact_book[new_name] = dict(phone_number = new_number, e_mail = new_mail, adress = new_adress)
            
            #ask if they want to add another new contact or not
            proceed = input("Do you wish to proceed? (y/n) ")
            if proceed =='y':
                continue
            elif proceed == 'n':
                break
            else:
                print("Enter choices 'y' or 'n'.")
               
                #block to delete contact
        elif choice == 'd':
            delete = input("Which contact do you wish to delete? ")
            del contact_book[delete]
            break
        else:
            print("Enter choices 'a' or 'd'.")
    
#display modified contact book
print("Modified contact book")
print(contact_book)