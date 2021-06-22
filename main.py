from math import sqrt


# Un programme qui calcul de résultat d'une équation du second degré


def calculEquation(a, b, c):
    s = 0
    delta = (b * b) - (4 * a * c)
    if delta > 0:
        s1 = (-b + sqrt(delta)) / (2 * a)
        s2 = (-b - sqrt(delta)) / (2 * a)
        s = str(s1) + " " + str(s2)
    elif delta == 0:
        s = -b / 2 * a
    return s


# resultat de l'équation
print(calculEquation(3, -6, 2))
