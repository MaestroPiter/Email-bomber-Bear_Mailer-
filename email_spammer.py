import smtplib
import os
os.system("color 4")
scelta="s"
nn=1
while scelta=="s":
    scelta2=int(0)
    while scelta2!=1 and scelta2!=2 and scelta2!=3:
        os.system("cls")
        print("EMAIL SPAMMER\n")
        aa="            ─────────────────────\n\
            ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n\
            ───█▒▒░░░░░░░░░▒▒█───\n\
            ────█░░█░░░░░█░░█────\n\
            ─▄▄──█░░░▀█▀░░░█──▄▄─\n\
            █░░█─▀▄░░░░░░░▄▀─█░░█"
        print(aa,"\n")
        print("Inserisci 1 se la mail da cui spammi è gmail")
        print("Inserisci 2 se la mail da cui spammi è outlook")
        print("Inserisci 3 se la mail da cui spammi è yahoo")
        scelta2=int(input("Scelgo: "))
    if scelta2==1:
        server="smtp.gmail.com"
        porta=int(587)
        print("ATTENZIONE: per mandare mail bisogna avere l'accesso ad app meno sicure sulle \
impostazioni dell'account.")
        scelta1=input("Vuoi controllare?[s/n] ")
        if scelta1=="s":
            os.system("start https://myaccount.google.com/u/2/lesssecureapps?pli=1&rapt=AEjHL4PZTzLLpNH")
    elif scelta2==2:
        server="smtp.live.com"
        porta=int(587)
    elif scelta2==3:
        print("ATTENZIONE: per mandare email, se si ha mail di recupero o verifica a 2 fattori, \
devi inserire una password temporanea per app.")
        scelta1=input("Vuoi controllare?[s/n] ")
        os.system("start https://login.yahoo.com/myaccount/security/app-password/?src=homepage&done=https%3A%2F%2Fit.yahoo.com%2F&scrumb=5VRwZcEPb4g")
        server="smtp.mail.yahoo.com"
        porta=int(587)
    os.system("cls")
    print("EMAIL SPAMMER\n")
    print(aa,"\n")
    utente=input("Inserisci il nome utente dell'account da cui vuoi mandare l'email: ")
    password=input("Inserisci la password dell'account da cui vuoi mandare l'email: ")
    destinatario=input("Inserisci l'account del destinatario che vuoi bombardare: ")
    messaggio=input("Inserisci il messaggio da mandare: ")
    n=int(input("Inserisci il numero di mail che vuoi mandare: "))
    a=input("Premi invio e parto a spammare")
    for i in range(0,n):
        email=smtplib.SMTP(server,porta)
        email.ehlo()
        email.starttls()
        email.login(utente,password)
        email.sendmail(utente,destinatario,messaggio)
        if nn==1:
            print(nn,"mail inviata")
        else:
            print(nn,"mail inviate")
        nn+=1
    email.close()
    scelta=input("Vuoi continuare ad utilizzare il programma?[s/n] ")
    os.system("cls")
