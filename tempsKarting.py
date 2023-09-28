def tableau_utilise() :
    tableau = 0
    while(tableau <= 0):
        tableau = int(input("Quel tableau voulez-vous utiliser ? \n\n Tapez 1 pour les temps de la course de karting \n Tapez 2 pour des temps personalisés \n choix: "))
        if(tableau > 2):
            print("Veuillez choisir entre le tableau 1 ou le tableau 2")
    return tableau


def saisie_valeurs() :
    nombre_temps = 0
    while (nombre_temps == 0):
        nombre_temps = int(input("\nCombien de temps voulez vous entrer ? \n"))
        if (nombre_temps <= 0 & nombre_temps != (-1)):
            print("Veuillez entrer au moins un temps !\n")
    groupe4 = []
    for i in range(nombre_temps):
        if(i == 0):
            print("Attention à bien utiliser le point pour les chiffres à virgules ;)\n")
        valeur = float(input(f"entrer le temps N°{i + 1}: "))
        groupe4.append(valeur)
    return groupe4


def conversion_temps(tableau_temps):
    tableau_secondes = []
    for minutes in tableau_temps:
        if minutes >= 1:
            secondes = round((minutes - 1) + 0.6, 2) * 100
        else:
            secondes = round(minutes, 2)
        tableau_secondes.append(secondes)
    return tableau_secondes


def fonction_meilleur_temps(tableau_secondes):
    for i in range(len(tableau_secondes)):
        temps = tableau_secondes[i]
        if i == 0 :
            meilleur_temps = temps
        elif  temps < meilleur_temps:
            meilleur_temps = temps
    return meilleur_temps


def print_minutes_secondes(meilleur_temps):
    minutes = meilleur_temps // 60
    secondes = meilleur_temps - 60
    print(f"\nLe meilleur temps est de {int(minutes)} minute et {int(secondes)} secondes. \n")


def demarage():
    tableau = tableau_utilise()
    if(tableau == 1):
        tableau_temps = [1.15, 1.18, 1.19, 1.19, 1.19, 1.20, 1.22, 1.22, 1.22, 1.23, 1.24, 1.25, 1.25, 1.26, 1.27, 1.29]
        tableau_secondes = conversion_temps(tableau_temps)
        meilleur_temps = fonction_meilleur_temps(tableau_secondes)
        print_minutes_secondes(meilleur_temps)

    elif (tableau == 2):
        tableau_temps = saisie_valeurs()
        tableau_secondes = conversion_temps(tableau_temps)
        meilleur_temps = fonction_meilleur_temps(tableau_secondes)
        print_minutes_secondes(meilleur_temps)

demarage()