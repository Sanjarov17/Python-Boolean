pin = input("PIN kodni kiriting: ")
correct_pin = "1234"

natija = pin != correct_pin or len(pin) != 4

print(natija)