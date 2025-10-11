earthWeight = float(input("What is your earth weight: "))
planet = int(input("What is your planet number: "))

if planet == 1:
    destination_weight = earthWeight * 0.38
    print(destination_weight)
elif planet == 2:
    destination_weight = earthWeight * 0.91
    print(destination_weight)
elif planet == 3:
    destination_weight = earthWeight * 0.38
    print(destination_weight)
elif planet == 4:
    destination_weight = earthWeight * 2.53
    print(destination_weight)
elif planet == 5:
    destination_weight = earthWeight * 1.07
    print(destination_weight)
elif planet == 6:
    destination_weight = earthWeight * 0.89
    print(destination_weight)
elif planet == 7:
    destination_weight = earthWeight * 1.14
else:
    print("Invalid Planet Number")
