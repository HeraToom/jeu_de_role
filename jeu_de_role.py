import random

#2 joueurs, nous et un enemi
# chacun à 50 point de vie
# 3 potions pour nous
# chaque potion permet de recuperer entre 15 et 50 point de vie
# notre attaque inflige entre 5 et 10 point de vie
# l'attaque ennemie elle inflige enre 5 et 15
#lorsque on utilise une potion notre tour est passé

#variable
potions_de_vie = 3
separateur = "-"*100
point_de_vie_joueur = 50
point_de_vie_ennemi = 50

while True:
    choix_joueur = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2)?")

    while not choix_joueur.isdigit():
        print("Faite un choix valide ! votre vie en dépend... respectez-vous !")
        choix_joueur = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2)?")
    else:
        choix_joueur_verifier = int(choix_joueur)

    if choix_joueur_verifier == 1:
        attaque_joueur = random.randint(5, 10)
        attaque_ennemi = random.randint(5, 15)
        point_de_vie_ennemi = point_de_vie_ennemi - attaque_joueur
        point_de_vie_joueur = point_de_vie_joueur - attaque_ennemi
        print(f"Vous avez infligé {attaque_joueur} point de dégats à l'ennemi ⚔️")
        print(f"L'ennemie vous as infligé {attaque_ennemi} point de dégats ⚔️")
        print(f"Il vous reste {point_de_vie_joueur} points de vie.")
        print(f"Il reste {point_de_vie_ennemi} à l'ennemi.")
        print(separateur)

    if choix_joueur_verifier == 2 and potions_de_vie > 0:
        potions_de_vie -= 1
        soin = random.randint(15, 50)
        attaque_ennemi = random.randint(5, 15)
        point_de_vie_joueur = point_de_vie_joueur + soin
        point_de_vie_joueur = point_de_vie_joueur - attaque_ennemi
        print(f"Vous avez récupérez {soin} points de vie ❤️ ({potions_de_vie} 🧪 restantes)")
        print(f"L'ennemie vous as infligé {attaque_ennemi} point de dégats ⚔️")
        print(f"Il vous reste {point_de_vie_joueur} points de vie.")
        print(f"Il reste {point_de_vie_ennemi} à l'ennemi.")
        print(separateur)
        if potions_de_vie:
            print("Vous passez votre tour...")
            attaque_ennemi = random.randint(5, 15)
            point_de_vie_joueur = point_de_vie_joueur - attaque_ennemi
            print(f"L'ennemie vous as infligé {attaque_ennemi} point de dégats ⚔️")
            print(f"Il vous reste {point_de_vie_joueur} points de vie.")
            print(f"Il reste {point_de_vie_ennemi} à l'ennemi.")
            print(separateur)

    if choix_joueur_verifier == 2 and potions_de_vie == 0:
        print("Vous n'avez plus de potions... bon courage")
        continue

    if point_de_vie_joueur < 1:
        print("L'ennmie à eu raison de vous... relevez-vous et recommencer 🎮")
        print("Fin du jeu.")
        break

    if point_de_vie_ennemi < 1:
        print("Vous avez gagné bravo, vous rentrez vous coucher car la journée n'as pas été de tous repos 😴")
        print("Fin du jeu.")
        break

