try:
    number = int(input("Enter a number:"))
    print("The number entersd is",number)


except ValueError as ex:
    print("Exception:", ex)