# Ülesanne 1: Tere Maailm ja kasutaja sisestus

"""# -*- coding: latin-1 -*-
print("Tere Maailm!")
nimi = input("Sisesta oma nimi: ")
print("Tere maailm! " + nimi + "!")
vanus = input("Kui vana sa oled? ")
print("Sa oled " + vanus + " aastat vana.")
kas_käib_koolis = input("Kas sa käid koolis? (jah/ei) ")
sugu = input("Mis sugu sa oled? (mees/naine) ")

if sugu.lower() == "mees":
    print("Tere, härra " + nimi + "!")
elif sugu.lower() == "naine":
    print("Tere, proua " + nimi + "!")
else:
    print("Tere, " + nimi + "!")
    print("Lõpetame programmi. Nägemist!")
    exit()

# Ülesanne 2: Andmetüübid

vanus = 18              #int 
eesnimi = "Jaak"        #string
pikkus = 1.65           #float
kas_käib_koolis = True  #bool
print(f"vanus {vanus} on: {type(vanus)}")
print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
print(f"pikkus {pikkus} on: {type(pikkus)}")
print(f"kas_käib_koolis {kas_käib_koolis} on: {type(kas_käib_koolis)}")

# Ülesanne 3: Muutujad ja sisend

from random import *
laua_peal=randint(10,50)
print(f"Laual on {laua_peal} kommi.")
võtab=int(input("Mitu kommi soovid võtta?"))
laua_peal-=võtab
print(f"Laual on nüüd {laua_peal} kommi")"""

# Ülesanne 4

from math import *
ümbermõõt = int(input("Sisesta puu ümbermõõt meetrites: "))
läbimõõt = ümbermõõt/3.14
print(f"Puu läbimõõt on {läbimõõt} meetrit.")
raadius = läbimõõt/2
pindala = 3.14*raadius**2
print(f"Puu pindala on {pindala} ruutmeetrit.")
ruumala = 4/3*3.14*raadius**3
print(f"Puu ruumala on {ruumala} kuupmeetrit.")

# Ülesanne 5
