# -*- coding: utf-8 -*-

from Boites import Boites
import matplotlib.pyplot as plt
import scipy.stats as sps
import numpy as py

'''
Les programs au-dessous correspondent les questions dans la partie Etude asymptotique, veuillez éffacer les signe de commentaire avant de “Run”
'''
'''***********************************************************************************************
 Question 1.7 la convergence vers p(k)
'''
# definir des variables necessaire

NOMBRE_BOULE = 10000  # nombre de boule qu'on pose
ALPHA = 0.6  # valeur d'alpha
b = Boites(NOMBRE_BOULE, ALPHA)  # intialise une classe boite
num = 1  # on cherche la convergence vers p(num), ici on prend num = 1 par exemple
p_num = []
valeur_asymptotique = []
b_temp = Boites(NOMBRE_BOULE, ALPHA)
p_theorique = b.probabiliteTheorique(num)
# afficher les resultats de p(bk) reel et p(k) theorique
for i in range(1, b.nombre_boule + 1):
    choixDeBoite = b.choisirBoite(i)
    b.mettreBouleDansBoite(choixDeBoite)
    if (len(b.boites) > num):
        p_num.append(b.boites[num - 1] / (b.alpha * i))
    else:
        p_num.append(0)
    valeur_asymptotique.append(p_theorique)
print (p_num[b.nombre_boule - 1])
plt.xlabel(r'$n$')
plt.ylabel(r'$F_n^{(1)}/\alpha n$')
plt.plot(range(b.nombre_boule), p_num, "r",
         label=r"$F_n^{(1)}/\alpha n$ $(n>0, \alpha=0.6, \rho=2.5)$")
plt.plot(range(b.nombre_boule), valeur_asymptotique, "g",
         label=r"$p(1)=40/693$")
plt.title(r'$F_n^{(1)}/\alpha n\rightarrow p(1)$')
plt.legend(loc='best')
plt.show()


'''******************************************************************************************
   Qestion 2.8  Simulation de la limite
'''
# afficher simulation de la question 1.8, convergence en loi
'''
MAX_NUM_BOULE = 1000  # nombre de boules qu'on pose
ALPHA = 0.6  # valeur d'alpha
NUM_REPETITION = 2000  # nombre de fois de répétition
num = 1  # la convegence qu'on verifie. ici on prenc num = 1, p(1) par exemple
resultat = []
b = Boites(MAX_NUM_BOULE, ALPHA)
p_num = b.probabiliteTheorique(num)
for i in range(NUM_REPETITION):
    b = Boites(MAX_NUM_BOULE, ALPHA)
    b.poseBoules()
    valeur = py.sqrt(MAX_NUM_BOULE) * (
        b.boites[num - 1] * 1.0 / (b.alpha * MAX_NUM_BOULE) - p_num)
    resultat.append(valeur)
x = py.linspace(-4, 4, 2000)
y = sps.norm.pdf(x)
# pour le cas où num = 1, cette variable converge ver une gaussienne centrée réduite
# et on peux décommenter la ligne ci-dessous
plt.plot(x, y, color="r", label=r"$N(0,1)$")
plt.hist(resultat, normed=1, bins=30)
plt.title(r'$Convergence$ $de$ $(\sqrt{n}(F_n^{(1)}/\alpha n-p(1)))$')
plt.xlabel(r'$n$')
plt.ylabel(r'$(\sqrt{n}(F_n^{(1)}/\alpha n-p(1)))$')
plt.legend(loc='best')
plt.show()
'''
