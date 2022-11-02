'''
Sintetizza delle immagini di dimensione 300*300 pixel da fornire come feedback all'utente.
'''
import cv2
import numpy as np

def sintImm(s):
    if type(s)==type("Stringa") and len (s)==9:
        immagine=quadrato(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8])
        cv2.imwrite("SINT.jpg",immagine)
        return immagine
    return np.zeros(1)
        
def L2C(l):
    if l=="U":
        return np.array([0,255,255])#giallo
    if l=="L":
        return np.array([0,0,204])#rosso
    if l=="R":
        return np.array([0,128,255])#arancione
    if l=="D":
        return np.array([255,255,255])#bianco
    if l=="F":
        return np.array([0,204,0])#verde
    if l=="B":
        return np.array([204,102,0])#blu
def quadrato(a,b,c,d,e,f,g,h,i):
    ret=[]
    misura=100
    r=[]
    for k in range(misura):
        r.append(L2C(a))
    for k in range(misura):
        r.append(L2C(b))
    for k in range(misura):
        r.append(L2C(c))
    for k in range(misura):
        ret.append(r)
    #
    r=[]
    for k in range(misura):
        r.append(L2C(d))
    for k in range(misura):
        r.append(L2C(e))
    for k in range(misura):
        r.append(L2C(f))
    for k in range(misura):
        ret.append(r)
    r=[]
    for k in range(misura):
        r.append(L2C(g))
    for k in range(misura):
        r.append(L2C(h))
    for k in range(misura):
        r.append(L2C(i))
    for k in range(misura):
        ret.append(r)
    return np.array(ret)  
sintImm("URFDLBFRU")
