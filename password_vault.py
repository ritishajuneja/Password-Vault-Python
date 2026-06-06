name=input("PLEASE ENTER YOUR NAME: ")
print("HELLO!",name,"Welcome to Rishu's Password Vault.")

user=input("login/signup?\n")

if user=="login":

    user_name=name
    password=input("Enter your password: \n")

    if password==user_name:

        print("Login successful 😊")

        choice=int(input("Please enter choice number from the following options available:\n1-VIEW ACCOUNTS\n2-SEARCH FOR AN ACCOUNT\n3-ADD NEW ACCOUNT\n"))

        if choice==1:

            with open("passwords.txt","r") as f:
                data=f.read()
                print(data)

        elif choice==2:

            n=input("Enter account name you want to search for: ")

            with open("passwords.txt","r") as f:
                data=f.read()

                if data.find(n)!=-1:
                    print("FOUND")
                else:
                    print("NOT FOUND")

        elif choice==3:

            item=int(input("How many accounts you want to enter?"))
            i=1

            while i<=item:

                acc_name=input("Enter account name: ")
                p=input("Enter account password: ")

                with open("passwords.txt","a") as f:
                    f.write("\n"+acc_name + ":" + p + "\n")

                i+=1

            print("Account added successfully!")

        else:

            print("INVALID CHOICE")

    else:

        print("WRONG PASSWORD")

elif user=="signup":

    create_pass=input("Enter your password: ")

    with open("users.txt","a") as f:
        f.write(name + ":" + create_pass + "\n")

    print("Account created 😊")
    print("Please refresh the page and login")

else:

    print("INVALID OPTION")