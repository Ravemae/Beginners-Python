''' ASSIGNMENT
# Create a registration form that collects the following
- Firstname
- Lastname
- Username
- Age
- Phone number
- Password1
- Password2 
- Print a Message saying
    (f"Dear {Firstname} & {Lastname}, Your account has '''
    
print('Welcome to Ferrostar Inc.\nPlease Fill In The Registration Form Below To Continue.😊')
firstname = str(input("Your Firstname\n>> ")).capitalize()
lastname = str(input("Your Lastname\n>> ")).capitalize()
Username = str(input("Your Username\n>> ")).lower()
Age = int(input("Your Age\n>> "))
email = (input("Your email\n>> "))
Phone_number = int(input("Your Phone Number\n>> "))
Password1 = (input("Your Password1\n>> "))
Password2 = (input("Your Password2\n>> "))
address = int(str(input("Your Address\n>> "))).upper()
dob = int(input("Your date of birth\n>> "))

print(f"Dear {firstname} {lastname}, Your account has been created")