import random
los = input("Podaj liczbę od 1 do 49, sprawdzimy, czy trafiłeś los: ")
losowana = random.randint(1,49)
print(losowana)
if int(los) == losowana:
    print("HURRA, TRAFIŁEŚ !!!!")
else:
    print("No niestety, nie trafiłeś!")


