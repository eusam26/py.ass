
def sign_up():
    while True:
        username = input("Enter your username: ")
        fullname = input("Enter your full name: ")
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")

        if password == confirm_password:
            print("\nSign up successful!")
            print("Username:", username)
            print("Full Name:", fullname)
            print("Password:", password)
            break
        else:
            print("\nPasswords do not match. Please try again.")

sign_up()
