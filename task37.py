pin = input("pin: ")
correct_pin = input("correct pin: ")

if pin != correct_pin or len(pin) != 4:
    print(True)
else:
    print(False)