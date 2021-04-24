import colorama
from colorama import Fore, Style, Back
colorama.init()
path = "Agenda/"
def SceltaAggiungi(f):
    while True:    
        print(Fore.CYAN +"\nVuoi aggiungere qualche impegno o vuoi tornare al menu principale?\n" + Fore.GREEN + "[Aggiungi] [Torna]\n" + Fore.LIGHTMAGENTA_EX)    
        scelta = input()
        if scelta == "Aggiungi" or scelta == "aggiungi":
            print(Fore.CYAN + "\nInserisci l'ora del impegno (lascia vuoto per non specificare) (Formato : HH:MM): \n" + Fore.LIGHTMAGENTA_EX)
            ora = input()
            print(Fore.CYAN + "\nInserisci la descrizione dell'impegno\n" + Fore.LIGHTMAGENTA_EX)
            descrizione = input()
            f.write("\n\nOra : " + ora + "\nDescrizione : " + descrizione)
        else:
            break
def LeggiImpegni(t):
    f = open(path + t + ".txt", "r")
    contenuto = f.read()
    print(Style.RESET_ALL + contenuto)
print(Fore.RED + "Grazie per aver scaricato Agenda 1.0!\nQuest'agenda si occupa di salvare i tuoi impegni e leggergli per te!\nPerche non fai una prova?" + Style.RESET_ALL)
while True:
    print(Fore.CYAN + "\nCosa vuoi fare?\n" + Fore.GREEN +"[Leggi impegni] [Annota impegni] [Esci]\n" + Fore.LIGHTMAGENTA_EX)
    operazione = input()
    if operazione == "Annota impegni" or operazione == "annota impegni": #Sistema di annotazione
        print(Fore.CYAN + "\nHai selezionato [Annota impegni]\nDesideri creare un nuovo gruppo di impegni o modificarne un altro?\n" + Fore.GREEN + "[Modifica] [Crea]\n" + Fore.LIGHTMAGENTA_EX)
        operazione_annota = input()
        if operazione_annota == "Crea" or operazione_annota == "crea": #Sistema di annotazione/Crea Gruppo di impegni
            print(Fore.CYAN + "\nInserisci il titolo del gruppo di impegni : \n" + Fore.LIGHTMAGENTA_EX)
            titolo = input()
            print(Fore.CYAN + "\ninserisci la data (formato DD/MM/AAAA): \n" + Fore.LIGHTMAGENTA_EX)
            data = input()
            f = open(path + titolo + ".txt", "w+")
            f.write("\nTitolo: " + titolo + "\nData degli impegni: " + data)
            print(Fore.CYAN + "\nGruppo di impegni creato con successo!")
            SceltaAggiungi(f)
            f.close()
        elif operazione_annota == "Modifica" or operazione_annota == "modifica": #Sistema di annotazione/Modifica Gruppo di impegni
            print(Fore.CYAN + "\nQuale gruppo di impegni desideri modificare ?\n" + Fore.LIGHTMAGENTA_EX)
            titolo = input()
            f = open(path + titolo + ".txt")
            SceltaAggiungi(f)
    elif operazione == "Leggi impegni" or operazione == "leggi impegni":
        print(Fore.CYAN + "\nQuale gruppo di impegni vuoi leggere?\n" + Fore.LIGHTMAGENTA_EX)
        Titolo = input()
        print("\n\n")
        LeggiImpegni(Titolo)
        print("\n\n")    
    elif operazione == "Esci" or operazione == "esci":
        exit()