import phonenumbers
from phonenumbers import carrier , geocoder , timezone



print("\033[91m" + ".____            ___________                     __                 ")
print("\033[91m" + "|    |           \__    ___/___________    ____ |  | __ ___________ ")
print("\033[91m" + "|    |      ______ |    |  \_  __ \__  \ _/ ___\|  |/ // __ \_  __ \ ")
print("\033[91m" + "|    |___  /_____/ |    |   |  | \// __ \\  \___|    <\  ___/|  | \/")
print("\033[91m" + "|_______ \         |____|   |__|  (____  /\___  >__|_ \\___  >__| ")  
print("\033[91m" + "        \/                             \/     \/     \/    \/      ")


print("[1] Mobile Tracker")
print("\n\n\n")

op = int(input("[+] "))













if op == 1:
    mobileNo = input("ENTER MOBILE NUMBER WITH COUNTRY CODE: ")
    mobileNo = phonenumbers.parse(mobileNo)

    #get timezone a phone number 
    print(timezone.time_zones_for_number(mobileNo))

    #getting a carrier for phonenumbers
    print(carrier.name_for_number(mobileNo,"en"))

    #getting region information
    print(geocoder.description_for_number(mobileNo, "en"))

    #validating a phonenumber
    print("VALID MOBILE NUMBER: ", phonenumbers.is_valid_number(mobileNo))

    #checking possibility of number
    print("Checking possibility of number...", phonenumbers.is_possible_number(mobileNo))