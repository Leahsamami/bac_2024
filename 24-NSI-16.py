# Ex1
def ecriture_binaire_entier_positif(n):
    resultat = ""
    while n > 0:
        resultat = str(n%2) + resultat
        n = n//2
    return resultat

# Ex2
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(1, n):
        for j in range(n):
            if tab[j] > tab[i]:
                echange(tab, j, i)
    return tab
