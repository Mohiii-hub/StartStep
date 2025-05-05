#Calculator
def Addition():
    try:
        eingabe1 = int(input("tipp dein erste Zahl Bitte:"))
        eingabe2 = int(input("tipp dein zweite Zahl Bitte:"))        
        ausgabe = eingabe1 + eingabe2
        print("dein Additionsergebnis ist=:",ausgabe)            
    except ValueError:   
        print("error eingabe ist nict Zahl")   

def Division():   
    try:
        eingabe1 = int(input("gib deine erste Zahl ein,Bitte: ",))
        eingabe2 = int(input("gib deine zweite Zahl ein,Bitte: ",))
        ausgabe = eingabe1 / eingabe2
        print("Dein Divisionergibnis ist=",ausgabe)              
    except ValueError:   
        print("error eingabe ist nict Zahl")   

def Subtraktion():
    try:
        eingabe1 = int(input("gib deine erste Zahl ein,Bitte: ",))
        eingabe2 = int(input("gib deine zweite Zahl ein,Bitte: ",))
        ausgabe = eingabe1 - eingabe2
        print("Dein Subtraktionsergibnis ist=",ausgabe)
    except ValueError:   
        print("error eingabe ist nict Zahl")   
def Multiplikation():
    try:
        eingabe1 = int(input("gib deine erste Zahl ein,Bitte: ",))
        eingabe2 = int(input("gib deine zweite Zahl ein,Bitte: ",))
        ausgabe = eingabe1 * eingabe2
        print("Dein Multiplikationergibnis ist=",ausgabe)
    except ValueError:   
        print("error eingabe ist nict Zahl")  

Addition()        
Division()  
Subtraktion()
Multiplikation()