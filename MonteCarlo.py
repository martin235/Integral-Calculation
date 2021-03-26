# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import random 
import math

def fonction(x):
    return x**4


def val(x1,x2,n):
    h=(x2-x1)/n
    mini=fonction(x1)
    maxi=fonction(x2)
    for i in range(n):
        f=fonction(x1+i*h)
        if f>maxi:
            maxi=f
        if f<mini:
            mini=f
    if mini>0:
        mini=0
    if maxi<0:
        maxi=0
    return mini,maxi



def MonteCarlo(x1,x2,n,precision):
    compteur=0
    valeur=val(x1,x2,precision)
    minimum=valeur[0]
    maximum=valeur[1]
    for i in range(n):
        x=random.uniform(x1,x2)
        y=random.uniform(minimum,maximum)
        y2=fonction(x)
        if y2>0:
            if y2>y:
                compteur+=1
        else:
            if y2<y:
                compteur-=1
    return (compteur/n)*abs(maximum-minimum)*(x2-x1)


def Integrale(x1,x2,n,rep,prec):
    prob=0
    for a in range(rep):
        prob+=MonteCarlo(x1,x2,n,prec)
    return prob/rep