yil = int(input("yilni kiriting"))

result = (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)

print(result)