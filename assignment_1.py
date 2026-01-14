# Uppgift 1

# Skriv ett program som

  #  skapar en variabel nice_name och tilldelar den värdet "Kim", samt skriver ut värdet på denna variabeln
  #  skapar en ny variabel long_name och tilldelar den värdet "KimKimKim..." (upprepat 33 gånger) genom att använda en for-slinga, samt skriver ut värdet på variabeln.

nice_name = "Kim"
print(nice_name)

long_name = ""
for i in range(33):
    long_name += nice_name
print(long_name)