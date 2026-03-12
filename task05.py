email = input("email: ")

if "@" in email and email.endswith(".com"):
    print(True)
else:
    print(False)