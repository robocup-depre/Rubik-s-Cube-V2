from RPi import GPIO
import time
GPIO.setmode(GPIO.BOARD)
step_=8
dir_=12

rele_=22

orario=GPIO.HIGH
antiorario=GPIO.LOW

b_=38
l_=40
d_=35
r_=37
f_=31
u_=29

enabled=GPIO.LOW
disabled=GPIO.HIGH

n_1=50
n_a=150
n_2=100

tempo=0.002
stabilizzazione=1.5

def isLetter(l):
    return l=="U" or l=="R" or l=="F" or l=="D" or l=="L" or l=="B"

def risolvi_tutto(soluzione):
    init()
    while len(soluzione)>2:
        face=soluzione[0]
        if soluzione[1]==" ":
            retti=1
            soluzione=soluzione[2:]
        elif soluzione[1]=="'":
            retti=-1
            soluzione=soluzione[3:]
        elif soluzione[1]=="2":
            retti=2
            soluzione=soluzione[3:]
        muovi(face,retti)
    face=soluzione[0]
    if len(soluzione)==1:
        retti=1
    elif soluzione[1]=="'":
        retti=-1
    elif soluzione[1]=="2":
        retti=2
    muovi(face,retti)
        
def muovi(f,r):
    azzera()
    print(f,r)
    #imposta il verso di rotazione e il numero di passi
    if r==1:
        n=n_1
        d=orario
    elif r==-1:
        n=n_a
        d=orario
    elif r==2:
        n=n_2
        d=orario
    GPIO.output(dir_,d)
    #abilita il motore corrispondente
    if f=="U":
        GPIO.output(u_,enabled)
    elif f=="R":
        GPIO.output(r_,enabled)
    elif f=="F":
        GPIO.output(f_,enabled)
    elif f=="D":
        GPIO.output(d_,enabled)
    elif f=="L":
        GPIO.output(l_,enabled)
    elif f=="B":
        GPIO.output(b_,enabled)
    #muove
    for i in range(n):
        GPIO.output(step_,GPIO.HIGH)
        time.sleep(tempo)
        GPIO.output(step_,GPIO.LOW)
        time.sleep(tempo)
    azzera()
    time.sleep(stabilizzazione)

def azzera():
    GPIO.output(u_,disabled)
    GPIO.output(r_,disabled)
    GPIO.output(f_,disabled)
    GPIO.output(d_,disabled)
    GPIO.output(l_,disabled)
    GPIO.output(b_,disabled)
    
def init():
    
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    #azzera tutti i pin e li imposta come uscite
    #enable pin
    GPIO.setup(u_,GPIO.OUT)
    GPIO.setup(r_,GPIO.OUT)
    GPIO.setup(f_,GPIO.OUT)
    GPIO.setup(d_,GPIO.OUT)    
    GPIO.setup(l_,GPIO.OUT)
    GPIO.setup(b_,GPIO.OUT)
    GPIO.setup(rele_,GPIO.OUT)
    azzera()
    #step and direction pin
    GPIO.setup(step_,GPIO.OUT)
    GPIO.setup(dir_,GPIO.OUT)
    #rele pin
    rele(1)
    
def t(s):
    risolvi_tutto(s)
    
def rele(stato):
    GPIO.output(rele_,stato)
    time.sleep(0.1)
#______________________________________________________________________#####
if __name__=="__main__":
    
    print("risolvi_tutto:=riceve la soluzione come stringa e muove i motori uno dopo l'altro")   
