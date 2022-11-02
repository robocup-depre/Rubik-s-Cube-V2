'''
Gestisce la color detection
'''
import cv2
import numpy as np

def colore(a):
    if a[1]<100 :
        return "D"
    else:
        diff_rosso=min([abs(0-a[0]),abs(180-a[0])])
        diff_arancione=abs(15-a[0])
        diff_giallo=abs(32-a[0])
        diff_verde=abs(56-a[0])
        diff_blu=abs(106-a[0])
        m=min([diff_rosso,diff_arancione,diff_giallo,diff_verde,diff_blu])
        if m==diff_rosso:
            return"L"
        if m==diff_arancione:
            return "R"
        if m==diff_giallo:
            return "U"
        if m==diff_verde:
            return "F"
        if m==diff_blu:
            return "B"
        else:
            return  "errore"
def apri_e_riconosci():
    nome="image.jpg"
    img_rgb=cv2.imread(nome)
    img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)
    dimy=len(img)
    dimx=len(img[1])
    s11=img[int(dimy/6)*1][int(dimx/6)*1]
    s21=img[int(dimy/6)*1][int(dimx/6)*3]
    s31=img[int(dimy/6)*1][int(dimx/6)*5]
    s12=img[int(dimy/6)*3][int(dimx/6)*1]
    s22=img[int(dimy/6)*3][int(dimx/6)*3]
    s32=img[int(dimy/6)*3][int(dimx/6)*5]
    s13=img[int(dimy/6)*5][int(dimx/6)*1]
    s23=img[int(dimy/6)*5][int(dimx/6)*3]
    s33=img[int(dimy/6)*5][int(dimx/6)*5]
    '''print(colore(s11),s11)
    print(colore(s21),s21)
    print(colore(s31),s31)
    print("\n")
    print(colore(s12),s12)
    print(colore(s22),s22)
    print(colore(s32),s32)
    print("\n")
    print(colore(s13),s13)
    print(colore(s23),s23)
    print(colore(s33),s33)
    print("\n")
    '''
    rit=cv2.resize(img_rgb,(500,500))
    stringa=""
    stringa=stringa+colore(s11)
    #stringa=stringa+"\n"
    stringa=stringa+colore(s21)
    #stringa=stringa+"\n"
    stringa=stringa+colore(s31)
    #stringa=stringa+"\n"
    
    stringa=stringa+colore(s12)
    #stringa=stringa+"\n"
    stringa=stringa+colore(s22)
    #stringa=stringa+"\n"
    stringa=stringa+colore(s32)
    #stringa=stringa+"\n"
    
    stringa=stringa+colore(s13)
    #stringa=stringa+"\n"
    stringa=stringa+colore(s23)
    #stringa=stringa+"\n"
    stringa=stringa+colore(s33)
    return stringa

def scrivi_file(contenuto):
    if type(contenuto)!=type("abc"):
        return 0
    nome_file=contenuto[4]
    nome_file=nome_file+".txt"
    file_scrittura=open(nome_file,"w")
    file_scrittura.write(contenuto)
    file_scrittura.close()
    return 1
if __name__=="__main__":
    print("colore\(a\):= analizza l'array HSV e restituisce il colore-White=D ecc...")
    print("apri_e_riconosci:=apre image.jpg e restituisce la stringa di colori")
    print("scrivi_file(contenuto):=scrive la stringa in un file di testo che si chiama con il colore del centro della faccia")
