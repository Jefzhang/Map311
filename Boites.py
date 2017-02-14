# -*- coding: utf-8 -*-

import numpy as py
import random


class Boites:

    # initialiser Boites
    def __init__(self, nombre_boule, alpha):
        self.alpha = alpha
        self.nombre_boule = nombre_boule
        self.rho = 1.0 / (1.0 - alpha)
        self.boites = []

    # choisir la boite ou on met la nouvelle boule
    def choisirBoite(self, n):
        # si le liste 'boite' n'est pas initialisee
        # on cree la premiere element du liste
        if len(self.boites) == 0:
            self.boites.append(0)
            return 0
        # condition ou on choisi une nouvelle boite
        r = random.random()
        if (r < self.alpha):
            return 0
        # condition ou on choisi des boites ayant une ou des boules
        destination = py.random.randint(1, n)
        sum_final = 0
        for i in range(0, len(self.boites)):
            # on choisit la boite par apport a la proportion
            sum_final = sum_final + self.boites[i] * (i + 1)
            if(sum_final >= destination):
                return i + 1

    # mettre une boule dans une boite choisie
    def mettreBouleDansBoite(self, n):
        # si n==0 on augmente le nombre de boites qui contiennent 1 boule.
        if n == 0:
            self.boites[0] += 1
        # si n est inferieur a la fin de liste
        # on diminue le nombre de boites qui contiennent n boules par un
        # on augmente celui qui contiennent n + 1 boules par un.
        elif n < len(self.boites):
            self.boites[n - 1] -= 1
            self.boites[n] += 1
        # si n est superieur a la fin de liste
        # on ajoute un nouvel element au liste
        # on refait la meme precedure que la condition precedente
        else:
            self.boites[n - 1] -= 1
            self.boites.append(1)

    # poser le nombre initialise de boules dans les boites
    def poseBoules(self, n=None):
        if n is None:
            for i in range(1, self.nombre_boule + 1):
                choixDeBoite = self.choisirBoite(i)
                self.mettreBouleDansBoite(choixDeBoite)
        else:
            num_artistes = 0
            i = 1
            while num_artistes < n:
                choixDeBoite = self.choisirBoite(i)
                i += 1
                if choixDeBoite == 0:
                    num_artistes += 1
                self.mettreBouleDansBoite(choixDeBoite)

    # calculer le resultat reel
    def calculerProbabilite(self, n):
        p_reel = []
        for i in range(len(self.boites)):
            p_reel.append(self.boites[i] * 1.0 /
                          (self.alpha * n))
        return p_reel

    # valeur theorique
    def probabiliteTheorique(self, k):
        p_k = self.rho / (1 + self.rho)
        if k >= 2:
            for i in range(1, k):
                p_k = p_k * i * 1.0 / (i + 1 + self.rho)
        return p_k
