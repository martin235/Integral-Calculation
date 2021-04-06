# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import random 
import math

def fonction(x,C=0):
    return math.exp(-x**2+2)+C

def derive(x,constante=0):
    h=1e-10
    return (fonction(x+h,constante)-fonction(x,constante))/h

def Newton(x,c=0,constante=0):
    a=derive(x,constante)
    if abs(a)<1e-06:
        return None
    Un=x-fonction(x,constante)/a
    if abs(Un-x)<1e-6:
        return Un
    elif c>2950:
        return None
    else:
        return Newton(Un,c+1,constante)

def Extremum(x1,x2,n):
    h=(x2-x1)/n
    mini=fonction(x1)
    maxi=fonction(x2)
    for i in range(n):
        f=fonction(x1+i*h)
        if f>maxi:
            maxi=f
        if f<mini:
            mini=f
    Majorant=math.ceil(maxi)+1
    Minorant=math.floor(mini)-1
    if Value(x1,x2,Newton(x1,0,-Majorant))==None and Value(x1,x2,Newton(x2,0,-Majorant))==None and Value(x1,x2,Newton(x1,0,Minorant))==None and Value(x1,x2,Newton(x2,0,Minorant))==None:
        return Majorant,Minorant


def Value(x1,x2,v):
    if v==None:
        return None
    if v<x1 and v>x2 :
        return None
def MonteCarlo(x1,x2,n,precision):
    compteur=0
    Maximum,Minimum=Extremum(x1,x2,precision)
    print(Maximum,Minimum)
    for i in range(n):
        x=random.uniform(x1,x2)
        y=random.uniform(0,Maximum+abs(Minimum))
        y2=fonction(x,abs(Minimum))
        if y2>=y:
            compteur+=1
    Mn=compteur/n
    print(Mn)
    return (x2-x1)*(Mn*Maximum+abs(Minimum)*(Mn-1)),(Mn*(1-Mn)/(n*0.004**2)*100)



def Integrale(x1,x2,n,prec):
    return MonteCarlo(x1,x2,n,prec)