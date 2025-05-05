#wandle Dezimal zu Bin <____>Bin zu Dezimal
def Bin_Dez():
    try:
        eingabe = input("gib dein Binäer Zahl:")
        ausgabe = int(eingabe,2)
        print("Dezimal Zahl ist:",ausgabe)
    except ValueError:
        print("error eingabe ist nict Binäer")

def Dez_Bin():
    try:
        eingabe = int(input("gib dein  Dezimal Zahl:"))
        ausgabe = bin(eingabe)[2:]
        print("Binäer Zahl ist:",ausgabe)
    except ValueError:
        print("Dein eingabe ist kein Dezimal Zahl")
Bin_Dez()
Dez_Bin()
