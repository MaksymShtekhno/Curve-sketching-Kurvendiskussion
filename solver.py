import sympy as sp


x = sp.Symbol('x')

# Funktion
#--------------------------------------------
function = x;

print("\nFUNCTION: ",function,";\n")
#--------------------------------------------




#Schritt 2 - Symmetrie

einsetzenPlusEins = function.subs(x,1)
einsetzenMinusEins = function.subs(x,-1)

if(einsetzenPlusEins==einsetzenMinusEins):
    print ("Achsensymmetrish;\n")
elif(einsetzenPlusEins == (einsetzenMinusEins*-1) ):
    print("Symmetrisch zu Ursprung;\n")
else:
    print("Keine Symmetrie erkennbar;\n")



#Schritt 3 - Vehfahren +-oo

print("VERFAHREN FUR + - oo:\n")

plus = function.subs(x, sp.oo)
minus = function.subs(x, -sp.oo)

print("X gegen Plus Unendlich = ",plus,";\n")
print("X gegen Minus Unendlich = ",minus,";\n")



# Schritt 4 Schnittpunkten mit Achsen

xSchnitt = sp.solveset(sp.Eq(function,0),domain=sp.S.Reals)
ySchnitt = function.subs(x,0)

print("SCHNITTPUNKTEN MIT ACHSEN:\n")

if(xSchnitt == sp.EmptySet()):
    print("Kein Schnittpunkten mit X-Achse;\n")
else:
    print("Mit X-Achsee: ", xSchnitt, ";\n")

if(ySchnitt == sp.EmptySet()):
    print("Kein Schnittpunkten mit Y-Achse;\n")
else:
    print("Mit Y-Achsee: ",ySchnitt,";\n")



#Schritt 5 Extremstellen

firstDiff = sp.diff(function)

mEST = sp.solveset(sp.Eq(firstDiff,0))

print("EXTREMSTELLEN\n")

print("Erste Ableitung: ",firstDiff,";\n")

if (mEST == sp.EmptySet()):
    print("Keine EST",";\n")
else:
    print("Mogliche Extremstellen: ", mEST,";\n")




#Schritt 6 Wendestellen und Bestatigung von mogliche Extremstellen


secondDiff = sp.diff(firstDiff)

if(mEST != sp.EmptySet):
    for kandidat in mEST:
        EST = secondDiff.subs(x, kandidat)
        if (EST > 0):
            print("MinStelle: ", kandidat, ";\n")
        elif (EST < 0):
            print("MaxStelle: ", kandidat, ";\n")
        elif (EST == 0):
            print("Nullstelle: ", kandidat, ";\n")


mWST = sp.solveset(sp.Eq(secondDiff,0))

print("Zweite Ableitung: ",secondDiff,";\n")

if (mWST == sp.EmptySet()):
    print("Keine WST",";\n")
else:
    print("Mogliche Wendestellen: ", mWST,";\n")

question = input("Do you want to calculate a square? (y/n)")
if(question=='y'):
    beg = input("Please, write a left border: ")
    end = input("Please, write a right border: ")
    res = sp.integrate(function,(x,beg,end))
    print(res)

