# �lesanne 1: Tere Maailm ja kasutaja sisestus

# -*- coding: latin-1 -*-
print("Tere Maailm!")
nimi = input("Sisesta oma nimi: ")
print("Tere maailm! " + nimi + "!")
vanus = input("Kui vana sa oled? ")
print("Sa oled " + vanus + " aastat vana.")
kas_k�ib_koolis = input("Kas sa k�id koolis? (jah/ei) ")
sugu = input("Mis sugu sa oled? (mees/naine) ")

if sugu.lower() == "mees":
    print("Tere, h�rra " + nimi + "!")
elif sugu.lower() == "naine":
    print("Tere, proua " + nimi + "!")
else:
    print("Tere, " + nimi + "!")
    print("L�petame programmi. N�gemist!")
    exit()

# �lesanne 2: Andmet��bid

vanus = 18              #int 
eesnimi = "Jaak"        #string
pikkus = 1.65           #float
kas_k�ib_koolis = True  #bool
print(f"vanus {vanus} on: {type(vanus)}")
print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
print(f"pikkus {pikkus} on: {type(pikkus)}")
print(f"kas_k�ib_koolis {kas_k�ib_koolis} on: {type(kas_k�ib_koolis)}")