etudiants = [
    {"nom": "Ali", "note": 15},
    {"nom": "Sara", "note": 12},
    {"nom": "Yanis", "note": 18},
    {"nom": "Lina", "note": 16}
]

while True:
    print("==Gestionnaire de Classe==")
    print("1. Voir les élèves")
    print("2. Voir la moyenne des notes")
    print("3. Voir le meilleur élève")
    print("4. Ajouter un élève")
    print("5. Quitter")

    choix = int(input("Séléctionnez un numéro: "))

    if choix == 1:
        for e in etudiants:

            print(e["nom"])
    elif choix == 2:
        somme = 0
        count = 0
        for e in etudiants:
            somme += e["note"]
            count += 1
        moyenne = somme / count
        print(moyenne)
    elif choix == 3:
        meilleur = etudiants[0]
        for e in etudiants:
            if e["note"] > meilleur["note"]:
                meilleur = e
        print(meilleur)

    elif choix == 4:
        nom = input("Nom: ")
        note = float(input("Note: "))
        etudiants.append({"nom": nom, "note": note})
    elif choix == 5:
        print("Au revoir")
        break
