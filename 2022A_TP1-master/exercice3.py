
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees, secondes= divmod(secondes,31536000)


    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines, secondes= divmod(secondes,6048000)


    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours, secondes= divmod(secondes,86400)


    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures, secondes= divmod(secondes,3600)


    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes, secondes= divmod(secondes,31536000)


    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
