price = input("Podaj cenę samochodu: ")
print("Koszt całkowity to: \n Cena samochodu",price, "zł\n" " + podatek 19% =", int(price)*0.19, "\n + opłata rejestracyjna 3% =", int(price)*0.03, "zł \n + prowizja przygotowawcza = 500zł \n + opłata za dostarczenie = 1000zł ")
print("===============\n RAZEM = ", int(price)+int(price)*0.19+int(price)*0.03+500+1000)



