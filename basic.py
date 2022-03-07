print("Siemano")
POWITANIE = "Witaj, swiecie Pythona!"
print(POWITANIE)

MESSAGE = "Ewelina"
print(MESSAGE)
MESSAGE = "Jestes super"  # type: str
print(MESSAGE)


print(MESSAGE.title())
print(MESSAGE.upper())
print(MESSAGE.lower())

NAME = "jakobs"
LASTNAME = "prokopski"

fullname = f"{NAME} {LASTNAME}"

print(f"\tSiemano, \ntutaj \n\t\t{fullname}")

TXT = "super                                      "
print(TXT)
TXT = TXT.rstrip()
print(TXT)

IMIE = "jakobs prokopski"

print(f"Hej {IMIE.title()}, co tam?")
FAMOUS_PERSON = "William Shakespeare"
print(f'"Byc czy nie byc - oto jest pytanie" \n - {FAMOUS_PERSON}')

x, y, z = 5, 6, 10
print(f"{x},{y},{z}")

print(7+24)
FAV = 7
# Mówi jaka jest moja ulubiona liczba
print(f"Moja ulubiona liczba to {FAV}")

print("haj")
INSTRUMENT = "pianino"
print(INSTRUMENT)
INSTRUMENT2 = "gitara"
LICZBA = 6 * 5

rhcp = ['frusciante', 'flea', 'chad', 'anthony']
print(f"Moim ulubionym gitarzystą jest {rhcp[0].upper()}")
print(rhcp[-1])

rhcp.append('navarro')
print(rhcp)
print(rhcp[-1])

pilkarze = []
pilkarze.append('lewandowski')
pilkarze.append('zidane')
pilkarze.append('salah')
print(pilkarze)

rhcp.insert(1, 'josh')
print(rhcp)
del rhcp[1]
print(rhcp)
popped_rhcp = rhcp.pop(1)
print(rhcp)
print(popped_rhcp)

guests = ['einstein', 'newton', 'kepler']
print(guests)
guests[2] = 'kopernik'
print(guests)
guests.insert(0, 'hawking')
guests.insert(2, 'hertz')
guests.append('jule')
print(guests)
popped_guest = guests.pop()
print(f"Przepraszam za brak zaproszenia dla {popped_guest}")
popped_guest = guests.pop()
print(f"Przepraszam za brak zaproszenia dla {popped_guest}")
popped_guest = guests.pop()
print(f"Przepraszam za brak zaproszenia dla {popped_guest}")
popped_guest = guests.pop()
print(f"Przepraszam za brak zaproszenia dla {popped_guest}")
print(guests)
del guests[0]
del guests[0]
print(guests)

auta = ['audi', 'bmw', 'toyota', 'subaru']
auta.sort()
print(auta)

places = ['london', 'paris', 'lisbon', 'madrid', 'budapest']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()


for member in rhcp:
    print(member)

pizza = ['hawajska', 'pepperoni', 'capriciosa']
for ulubiona_pizza in pizza:
    print(f"{ulubiona_pizza} jest moja ulubiona pizza")
print("Bardzo lubie pizze!")
