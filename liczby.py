numbers = list(range(1, 8))
print(numbers)
numbers.sort(reverse=True)
print(numbers)
parzyste = list(range(2, 22, 2))
print(parzyste)

kwadraty = []
for wartosc in range(0, 10, 3):
    kwadraty.append(wartosc**2)
del kwadraty[0]
print(kwadraty)
print(sum(kwadraty))

kwadraty_fancy = [kwadrat**2 for kwadrat in range(1, 8)]
print(kwadraty_fancy)

# zadanka
milion = list(range(1, 1_000_000+1))
print(min(milion))
print(max(milion))
print(sum(milion))

nieparzyste = list(range(1, 20+1, 2))
print(nieparzyste)

trzy = [liczba**3 for liczba in range(3, 30+1)]
print(trzy)

szescian = [liczba**3 for liczba in range(1, 11)]
print(szescian)

jedzonko = ['kebab', 'pizza', 'spaghetti', 'nalesniki', 'tofu', 'ryz', 'jablko', 'pomarancz']

print(f"Pierwsze elementy list to {jedzonko[0:4]}")

jedzonko_mod = jedzonko[:]

jedzonko_mod.append('ciastko')


print(jedzonko, jedzonko_mod)

for potrawa in jedzonko_mod:
    print(potrawa)

cars = ['audi', 'bmw', 'toyota', 'kia', 'nissan']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if 'subaru' not in cars:
    print("nie ma audi")
else:
    print("jest audi")

alien_color = ['zolty', 'zielony', 'czerwony']
for kolor in alien_color:
    if kolor == 'zielony':
        print("Otrzymujesz 5 punktow")
    elif kolor == 'zolty':
        print("Otrzymujesz 10 punktow")
    else:
        print("Otrzymujesz 15 punktow")

osoby = [56, 2, -3, 89, 22, 13]
for age in osoby:
    if age <= 0:
        print("Error - wiek nie moze byc mniejszy/rowny zeru 0")
    elif age < 2:
        print("Niemowlecie")
    elif 2 <= age < 4:
        print("Dziecko, ktore uczy sie chodzic")
    elif 4 <= age < 13:
        print("Dziecko")
    elif 13 <= age < 20:
        print("Nastolatek")
    elif 20 <= age < 65:
        print("Dorosly")
    elif 65 <= age < 120:
        print("Senior")
    else:
        print("Error - czlowiek nie zyje wiecej niz 120 lat")
