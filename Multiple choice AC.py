print("Wat is jouw naam: ")
naam = input("Naam: ")

print ("Hello " + naam)
print ()
print ("Het is leuk je te ontmoeten,laten we elkaar leren kennen.")
print ("Mijn naam is Yair, Ik ben jouw friend vanaf nu.")
print ()
print ("Welke is jouw favorite Ben & Jerry's?")

while True: 
    d1a = input("Is het?: A) Chocola. B) Rocky road. C) vanille. D) Geen van de bovengenoemde. [A/B/C/D]? ")
    if d1a in ['A', 'B', 'C', 'D']:
        break 
if d1a == "A":
    print ("Chocola.")
    print ("wat leuk, ik hou ook van chocola!")
elif d1a == "B":
    print ("Rockey road.")
    print ("prima keuze, ik kan de smaak van niet ontkennen van Rockey road.")
elif d1a == "C":
    print ("Vanille")
    print ("duidelijk en eenvoudig, kan er niet mis mee gaan.")
elif d1a == "D":
    print ("is het Geen van de bovengenoemde? wat is het dan?")  
    ijs = input ("   ")
    print (ijs, "fijne keuze.")
print ()
print ("Het was leuk om je te leren kennen!")
print ("Dat allemaal van mij, tot ziens")