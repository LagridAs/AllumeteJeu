#########################################################################
def afficher_allumettes(n):
        print("o  "*n)
        print("|  "*n)


#########################################################################
# nom : jeu_ordi
# valeurs entree : nb_allum et prise_max, nombre d'allumette en jeu et
# nombre d'allumette que l'on peut prendre au plus.
# valeurs sortie : prise, nombre d'allumettes prises.
# fonction : retourne la meilleure prise à faire
#########################################################################
def jeu_ordi(nb_allum, prise_max):
    prise = 0
    s = prise_max + 1
    t = (nb_allum - s) % (prise_max + 1)
    while (t != 0):
        s -= 1
        t = (nb_allum - s) % (prise_max + 1)
        prise = s - 1
    if (prise == 0):
        prise = 1
    return prise


#########################################################################
# nom : main
# fonction : initialiser le jeu et l'organiser.
#########################################################################
def main():
    # initialisation des variables.
    nb_max_d = 0  # nbre d'allumettes maxi au départ
    nb_allu_max = 0  # nbre d'allumettes maxi que l'on peut tirer au maxi
    nb_allu_rest = 0;  # nbre d'allumettes restantes
    prise = 0  # nbre d'allumettes prises par le joueur
    qui = -1  # qui joue? 0=User --- 1=PC
    # verification pour l'initialisation.
    while (nb_max_d < 10 or nb_max_d > 60):
        try:
            nb_max_d = int(input("Entrez un nombre max d'allumette au depart entre 10 et 60. "))
        except:
            print("saisie incorrecte")
        # mise a jour du nombre d'allumette en jeu.
    nb_allu_rest = nb_max_d
    afficher_allumettes(nb_allu_rest)
    while (nb_allu_max <= 0 or nb_allu_max > nb_max_d ):
        try:
            nb_allu_max = int(input("Entrez un nombre max d'allumette que l'on peut tirer au maxi %d " % nb_max_d))
        except:
            print("saisie incorrecte")
        # mise a jour du nombre d'allumette en jeu

    while (qui != 0 and qui != 1):
        try:
            qui = int(input("qui joue? User=0 et Pc=1 "))
        except:
            print("saisie incorrecte")
        # mise a jour du nombre d'allumette en jeu
    else:
        if (qui == 0):
            print("Le USER va commencer le jeu")
        else:
            print("Le PC va commencer le jeu")



    while (nb_allu_rest> 1):
        if (qui == 0):
            while (1):
                    prise = int(input("Entrer le nbr d'element que vous voulez prendre de %d d'allumettes qui rest " % nb_allu_rest))
                    if(prise<= nb_allu_max and prise>0):
                        nb_allu_rest = nb_allu_rest - prise
                        print("nbr d'allumettes qui reste est %d " % nb_allu_rest)
                        afficher_allumettes(nb_allu_rest)
                        if (nb_allu_rest == 1):
                            print("Pc a perdu")
                            break

                        qui = 1
                        prise = 0
                        break
                    else:
                        print("vous devez prende un nbr d'allumettes inferieure a %d" %nb_allu_max)
        else:
                prise= jeu_ordi(nb_allu_rest, nb_allu_max)
                print("Pc a pris %d " %prise)
                nb_allu_rest =nb_allu_rest - prise
                print("nbr d'allumettes qui reste est %d " % nb_allu_rest)
                afficher_allumettes(nb_allu_rest)
                qui = 0
                prise = 0
                if (nb_allu_rest == 1):
                    print("USER a perdu")

    else:
        print("La fin du jeu ")


if __name__ == "__main__":
    main()
