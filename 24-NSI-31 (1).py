def multiplication(n1, n2):
    if n1 <= n2:
        nbre_addition = n2
        n2 = n1
    else:
        nbre_addition = n1
        n1 = n2
    while nbre_addition > 1:
        n1 = n1 + n2
        nbre_addition -= 1
    while nbre_addition < 1:
        n1 = n1 - n2
        nbre_addition += 1
    return n1


# Ex2
def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False



