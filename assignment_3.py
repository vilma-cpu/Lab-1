# Uppgift 3

# Skriv ett program som frågar "Vad heter du?" tar emot en sträng från tangentbordet, och skriver ut en hälsning (T.ex. "Hej Kalle" om namnet var Kalle). Programmet skall upprepa frågan och tillhörande hälsning, ända tills namnet från tangentbordet är "Sauron". Då skall programmet skriva "Hej då" och inte fråga mer.

name = None

while name != "Sauron":
    name = input("Vad heter du? ")
    if name != "Sauron":
        print("Hej", name)

print("Hej då")
