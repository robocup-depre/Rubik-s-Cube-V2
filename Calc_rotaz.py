import kociemba

def rotate(face):#ruota di 90 gradi la faccia in input e la ritorna
    #angoli
    temp=face[0][0]
    face[0][0]=face[2][0]
    face[2][0]=face[2][2]
    face[2][2]=face[0][2]
    face[0][2]=temp
    
    #lati
    temp=face[1][0]
    face[1][0]=face[2][1]
    face[2][1]=face[1][2]
    face[1][2]=face[0][1]
    face[0][1]=temp
    
    #centro
    pass
    return face

def calcola(U,R,F,D,L,B):#riceve le facce (ipotizzate dritte) e ritorna la soluzione, serve anche per capire se le facce sono dritte
    stringa=""
    for riga in U:
        for elem in riga:
            stringa=stringa+elem
    for riga in R:
        for elem in riga:
            stringa=stringa+elem
    for riga in F:
        for elem in riga:
            stringa=stringa+elem
    for riga in D:
        for elem in riga:
            stringa=stringa+elem
    for riga in L:
        for elem in riga:
            stringa=stringa+elem
    for riga in B:
        for elem in riga:
            stringa=stringa+elem  
    sol=kociemba.solve(stringa)
    return sol
    

def raddrizza(u,r,f,d,l,b):#riceve le facce(string dai txt) storte e fa i tentativi per raddrizzarle
    U=[]
    U.append([u[0],u[1],u[2]])
    U.append([u[3],u[4],u[5]])
    U.append([u[6],u[7],u[8]])
    R=[]
    R.append([r[0],r[1],r[2]])
    R.append([r[3],r[4],r[5]])
    R.append([r[6],r[7],r[8]])
    F=[]
    F.append([f[0],f[1],f[2]])
    F.append([f[3],f[4],f[5]])
    F.append([f[6],f[7],f[8]])
    D=[]
    D.append([d[0],d[1],d[2]])
    D.append([d[3],d[4],d[5]])
    D.append([d[6],d[7],d[8]])
    L=[]
    L.append([l[0],l[1],l[2]])
    L.append([l[3],l[4],l[5]])
    L.append([l[6],l[7],l[8]])
    B=[]
    B.append([b[0],b[1],b[2]])
    B.append([b[3],b[4],b[5]])
    B.append([b[6],b[7],b[8]])
    
    contatore=0
    valide=[]
    sol_parziale="!!!"
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                for c4 in range(4):
                    for c5 in range(4):
                        for c6 in range(4):
                            U=rotate(U)
                            try:
                                sol_parziale=calcola(U,R,F,D,L,B)
                                contatore=contatore+1
                                valide.append([c1,c2,c3,c4,c5,c6])
                            except:
                                pass
                        R=rotate(R)
                    F=rotate(F)
                D=rotate(D)
            L=rotate(L)
        B=rotate(B)
    return contatore,valide,sol_parziale
if __name__=="__main__":
    print("rotate\(face\):=restituisce la faccia in input ruotata di 90 gradi per fare la ricostruzione dell'orientamento")
    print("calcola:=\(U,R,F,D,L,B):= prende le facce non necessariamente dritte e calcola la soluzione; solleva un'eccezione che viene catturata da raddrizza\(\)")
    print("raddrizza\(u,r,f,d,l,b):= fa 4096 combinazioni di rotazione delle facce per trovare le rotazioni giuste; restituisce il numero di soluzioni, tutte le soluzioni e l'ultima che ha trovato")
