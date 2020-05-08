import random


def check_details():
    print("please provide")
    username = str.upper(input("username: "))
    password = str.upper(input("password: "))
    staff = open("staff.txt", "r")
    info = staff.read()
    login_info = info.split()
    if username == login_info[0] and password == login_info[1] or username == login_info[6] and password == login_info[7]:
        print("login successful")
        session = open("session.txt", "w")
        session.write(f"{username} logged in successfully")
        session.close()
        options = True
        while options:
            print(f"hello {username}, what would you like to do? ")
            print(" ")
            print("1. create new account")
            print("2. check account details")
            print("3. logout")
            choice = str(input("press 1,2 or 3 to select preferred option: "))
            if choice == "1":
                print("please enter the following")
                acct_name = str.upper(input("account name: "))
                open_bal = str(input("opening balance: "))
                acct_type = str.upper(input("account type: "))
                acct_email = str.upper(input("account email: "))
                acct_number = random.randint(1000000000, 9999999999)
                details = open("customer.txt", "w")
                acct_details = f"{acct_name} {open_bal} {acct_type} {acct_email} {acct_number}"
                details.write(acct_details)
                details.close()
                print("account created successfully")
                print(f"your account number is {acct_number}")

            elif choice == "2":
                account_number = (input("please enter customer's 10 digit account number: "))
                det = open("customer.txt", "r")
                the_details = det.read()
                get_details = the_details.split()
                if account_number in get_details:
                    print(get_details)
                else:
                    print("The account number does not match any account in our records.")
                    print("please check and try again or create new account")

            elif choice == "3":
                close_session = open("session.txt", "w").close()
                options = False

            else:
                print("invalid entry. Please select 1, 2 or 3")

    else:
        print("incorrect username or password. Please check and try again")


print("Welcome to Dragon bank")
staff1_username = "DONLARJE"
staff1_password = "LIONEL10"
staff1_email = "frank@gmail.com"
staff1_fullname = "Eze Franklin C"

staff2_username = "FAV"
staff2_password = "FAV2002"
staff2_email = "mysweetness@gmail.com"
staff2_fullname = "Arumeze Favour M"

staff_record = open("staff.txt", "w")
staff_details = f"{staff1_username} {staff1_password} {staff1_email} {staff1_fullname} {staff2_username} {staff2_password} {staff2_email} {staff2_fullname}"
staff_record.write(staff_details)
staff_record.close()

login = True
while login:
    operation = str(input("For Staff login, press 1. To close app, press 2: "))

    if operation == "1":
        check_details()

    elif operation == "2":
        login = False

    else:
        print("invalid entry. Please select 1 or 2")
