logged_in = input('(True/False): ')
session_time = int(input('session_time: '))

if logged_in == 'False' or session_time == 0:
    print(True)
else:
    print(False)