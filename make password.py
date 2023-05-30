import random
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
password_length = int(input("Enter the password length: "))
if password_length < 6:
    print("The password length must be at least 6 characters.")
    exit()
password = "".join(random.choice(alphabet) for i in range(password_length))
print(password)

