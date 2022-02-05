# Rekursive Explorationsfunktion
def explore(d,Weight,Value):
    global opt
    if (Weight > C): # Falls Kapazität überschritten: Backtrack
        return
    if (Value > opt): # Falls neues Optimum gefunden: speichern
        opt = Value
    if (d < n): # Falls noch Gegenstände übrig:
        explore(d+1,Weight+w[d],Value+v[d])
        explore(d+1,Weight,Value)

# Definition des Rucksackproblems
n = 5 # Anzahl der Gegenstände
C = 20 # Kapazität des Rucksacks
w = [12,11,7,10,9] # Gewicht der Gegenstände
v = [420,380,290,360,320] # Wert der Gegenstände

# Hauptprogramm
opt = 0 # Wert der besten Lösung
explore(0,0,0) # Starte die Rekursion
print(opt) # Zeige Ergebnis
