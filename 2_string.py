tekst = "Anna, paweł, TomEK"

lista = tekst.split(", ")
print(tekst)
print(lista)
imie = lista[0]
print(imie)
print(type(lista))

imieDuze = imie.upper()
print(imieDuze)

imieMale = imie.lower()
print(imieMale)


#sprawdzanie zawartosci
zawartosc = imie.isalpha()
print(zawartosc)

imie = ""
zawartosc = imie.isalpha()
print(zawartosc)

imie = "Julia"
print("\nDane Uzytkownika:\nMasz na imie: "+imie)

tekst1 = "Jan\n"
tekst2 = "Nowak"

print(tekst1 + tekst2)

tekst1 = tekst1.rstrip()
print(tekst1 + tekst2)
print(tekst1 + " " + tekst2)

#wyswietlanie lancucha znakow

#wszystkie wersje Pythona
text = "%s, Java i %s"%("PHP", "PYTHON")
print(text)

#nowsze werjse pythona 2.6+
text = "{0}, Java i {1}".format("php", "python")
print(text)

#help(text.replace)
new = text.replace("PHP", "C#")
print(new)


#wypisanie danych
rok = "2019"
miesiac = "Marzec"
dzien = "23"

print("Data: ", end="")
print(dzien, miesiac, rok + "r")

print("Data: ", end="")
print(dzien, miesiac, rok + "r", sep="-")







print("\n")
