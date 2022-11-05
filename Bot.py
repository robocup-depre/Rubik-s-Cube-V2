'''
Programma principale: bot che riceve comandi o fotografie. Deve essere avviato all'accensione del raspberry e contiene anche un comando per spegnerlo.
'''
import telebot
import cv2
import numpy as np
import Colors_text as aux
import Calc_rotaz as rotaz
import os
import Motors as mot
import Sint as sint
bot=telebot.TeleBot("__insertYourTokenHere__",parse_mode=None)
password="__insertYourPasswordHere__"
@bot.message_handler(commands=['risolvi'])
def send_welcome(message):
    if check_id(message.chat.id):
        #caso id conosciuto
        #controlla se ci sono tutte le 6 facce (txt)
        if os.path.isfile("U.txt") and os.path.isfile("R.txt") and os.path.isfile("F.txt") and os.path.isfile("D.txt") and os.path.isfile("L.txt") and os.path.isfile("B.txt"):
            U_file=open("U.txt","r").readlines()[0]
            R_file=open("R.txt","r").readlines()[0]
            F_file=open("F.txt","r").readlines()[0]
            D_file=open("D.txt","r").readlines()[0]
            L_file=open("L.txt","r").readlines()[0]
            B_file=open("B.txt","r").readlines()[0]
            
            #conversione da stringa a lista:
            U=[]
            U.append([U_file[0],U_file[1],U_file[2]])
            U.append([U_file[3],U_file[4],U_file[5]])
            U.append([U_file[6],U_file[7],U_file[8]])
            R=[]
            R.append([R_file[0],R_file[1],R_file[2]])
            R.append([R_file[3],R_file[4],R_file[5]])
            R.append([R_file[6],R_file[7],R_file[8]])
            F=[]
            F.append([F_file[0],F_file[1],F_file[2]])
            F.append([F_file[3],F_file[4],F_file[5]])
            F.append([F_file[6],F_file[7],F_file[8]])
            D=[]
            D.append([D_file[0],D_file[1],D_file[2]])
            D.append([D_file[3],D_file[4],D_file[5]])
            D.append([D_file[6],D_file[7],D_file[8]])
            L=[]
            L.append([L_file[0],L_file[1],L_file[2]])
            L.append([L_file[3],L_file[4],L_file[5]])
            L.append([L_file[6],L_file[7],L_file[8]])
            B=[]
            B.append([B_file[0],B_file[1],B_file[2]])
            B.append([B_file[3],B_file[4],B_file[5]])
            B.append([B_file[6],B_file[7],B_file[8]])
            
            #raddrizza le facce
            n,conf_ok,sol_parziale=rotaz.raddrizza(U_file,R_file,F_file,D_file,L_file,B_file)
            messaggio_risposta="La sequenza risolutiva è:\n"+sol_parziale
            bot.reply_to(message,messaggio_risposta)
            mot.risolvi_tutto(sol_parziale)
        else:
            bot.reply_to(message, "mancano_facce")
    else:
        #caso id sconosciuto
        bot.reply_to(message,"ID sconosciuto. Digitare la password per poter utilizzare questo bot.")

@bot.message_handler(content_types=['photo'])
def photo(message):
    if check_id(message.chat.id):
        #inizio
        #salva_foto
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        #legge i colori
        stringa=aux.apri_e_riconosci()
        chat_id=message.chat.id
        sint.sintImm(stringa)
        foto=open("SINT.jpg",'rb')
        bot.send_photo(chat_id,foto)
        #salva i colori nel file di testo
        aux.scrivi_file(stringa)
        #salva una copia della foto
        nome_copia_foto=stringa[4]+".jpg"
        with open(nome_copia_foto, 'wb') as new_file:
            new_file.write(downloaded_file)
        #fine
    else:
        bot.reply_to(message,"ID sconosciuto. Digitare la password per poter utilizzare questo bot.")
        
def check_id(id):
    id_list=open("id_list.txt","r")
    for row in id_list:
        if str(id) == row:
            return 1
    return 0

def check_psw(id,psw):
    if psw==password:
        if not check_id(id):
            id_list=open("id_list.txt","a")
            id_list.write("\n")
            id_list.write(str(id))
            print(str(id) + " aggiunto a id_list")
        return 1
    return 0

@bot.message_handler(commands=['show'])
def show(message):
    if check_id(message.chat.id):
        #inizio check
        chat_id=message.chat.id
        for f in ["U","R","F","D","L","B"]:
            stringa=open(f+".txt","r").readlines()[0]
            sint.sintImm(stringa)
            foto=open("SINT.jpg",'rb')
            bot.send_photo(chat_id,foto)
        #fine check
    else:
        bot.reply_to(message,"ID sconosciuto. Digitare la password per poter utilizzare questo bot.")
@bot.message_handler(commands=['off'])
def shutd(message):
    if check_id(message.chat.id):
        mot.rele(0)
        os.system('sudo shutdown now')
    else:
        bot.reply_to(message,"ID sconosciuto. Digitare la password per poter utilizzare questo bot.")
@bot.message_handler(content_types=['text'])
def move(message):
    if not check_psw(message.chat.id,message.text):
        if check_id(message.chat.id):
            try:
                mot.risolvi_tutto(message.text)
                bot.reply_to(message,message.text)
            except:
                bot.reply_to(message,"Sequenza non valida")
        else:
            bot.reply_to(message,"ID sconosciuto. Digitare la password per poter utilizzare questo bot.")
#______________________________________________________________________________________________________________________________
print("Started...")
bot.infinity_polling()
