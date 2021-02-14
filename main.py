from GeneratePassword import generate_password
import json

while True:

    print("Enter option"
          + "\n1. Add"
          + "\n2. Edit"
          + "\n3. Search"
          + "\n4.Exit")
    option = int(input())

    if option == 1:
        item = {'website_name': input("Enter website name : "), 'mail_id': input("Enter the mail id : ")}
        pass_len = int(input("Enter the length of password : "))
        item['pass_str'] = ""
        while True:
            item['pass_str'] = generate_password(pass_len)
            print("Generated password is ", item['pass_str'])
            is_ok = int(input("If OK, press 1 else if you want to generate another press 0\n Option : "))
            if is_ok == 1:
                break

        # print(item)
        file = open("passwords.json", "r")
        items = []
        # print(file.read())
        if file.read() != "":
            file.seek(0)
            items = json.load(file)
        file.close()

        file = open("passwords.json", "w")
        items.append(item)
        print("Items : ", items)
        json.dump(items, file, indent=4)
        file.close()

    if option == 3:
        print("Search by "
              + "\n1. url"
              + "\n2. mail id")
        choice = int(input("Option : "))
        if choice == 1:
            url = input()
            file = open("passwords.json", "r")
            items = json.load(file)
            file.close()
            for item in items:
                if item['website_name'].lower().strip().__contains__(url.lower().strip()):
                    print("URL is : ", item['website_name'])
                    print("mail id is : ", item['mail_id'])
                    print("Password is : ", item['pass_str'])

        elif choice == 2:
            mail_id = input()
            file = open("passwords.json", "r")
            items = json.load(file)
            file.close()
            for item in items:
                if item['mail_id'].lower().strip().__contains__(mail_id.lower().strip()):
                    print("URL is : ", item['website_name'])
                    print("mail id is : ", item['mail_id'])
                    print("Password is : ", item['pass_str'])

    if option == 4:
        exit(1)
