from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()
root.title("Mój program")

lp = ()
listapunktow = StringVar()
otw_ety_txt = StringVar()
zap_ety_txt = StringVar()
kod_obiektu_txt = StringVar()
krg_n_v = StringVar()
krg_d_v = StringVar()
mppd_nd_v = StringVar()
nsz_v = StringVar()
dtp_v = StringVar()
blp_nd_v = StringVar()
remarks_v = StringVar()


def GSPPRB(*args):
    global f2
    f2.destroy()
    f2 = ttk.Frame(f)
    f2.grid(row=1, column=3, rowspan=6, sticky=(W, S, N, E))

    KRG_n = ttk.Label(f2, text="Id zgłoszenia lub KERG: ", padding=5)
    KRG_n.grid(row=0, column=0, sticky=W)
    KRG_n_wpis = ttk.Entry(f2, textvariable=krg_n_v)
    KRG_n_wpis.grid(row=0, column=1, sticky=(W, E))
    KRG_d = ttk.Label(f2, text="Id zgłoszenia lub KERG.Opis: ", padding=5)
    KRG_d.grid(row=1, column=0, sticky=W)
    KRG_d_wpis = ttk.Entry(f2, textvariable=krg_d_v)
    KRG_d_wpis.grid(row=1, column=1, sticky=(W, E))

    MPPD_nd = ttk.Label(f2, text="Metoda pozyskania danych: ", padding=5)
    MPPD_nd.grid(row=2, column=0, sticky=W)
    MPPD_nd_wpis = ttk.Combobox(f2, state="readonly", textvariable=mppd_nd_v)
    MPPD_nd_wpis.grid(row=2, column=1,  sticky=(W, E))
    MPPD_nd_wpis.configure(values=pozyskania)

    NSZ= ttk.Label(f2, text="Numer szkicu: ", padding=5)
    NSZ.grid(row=3, column=0, sticky=W)
    NSZ_wpis = ttk.Entry(f2, textvariable=nsz_v)
    NSZ_wpis.grid(row=3, column=1,  sticky=(W, E))

    DTP = ttk.Label(f2, text="Data pozyskania danych (rrrr-mm-dd): ", padding=5)
    DTP.grid(row=4, column=0, sticky=W)
    DTP_wpis = ttk.Entry(f2, textvariable=dtp_v)
    DTP_wpis.grid(row=4, column=1, sticky=(W, E))

    BLP_nd = ttk.Label(f2, text="Błąd położenia punktu: ", padding=5)
    BLP_nd.grid(row=5, column=0, sticky=W)
    BLP_nd_wpis = ttk.Combobox(f2, state="readonly", textvariable=blp_nd_v)
    BLP_nd_wpis.grid(row=5, column=1, sticky=(W, E))
    BLP_nd_wpis.configure(values=blad)

    remarks = ttk.Label(f2, text="Uwagi: ", padding=5)
    remarks.grid(row=6, column=0, sticky=W)
    remarks_wpis = ttk.Entry(f2, textvariable=remarks_v)
    remarks_wpis.grid(row=6, column=1, sticky=(W, E))

    generator = ttk.Button(f2, text="Generuj", command=gener)
    generator.grid(row=7, column=1, sticky=W)


def COS(*args):
    f2 = ttk.Frame(f)
    f2.grid(row=1, column=3, rowspan=6, sticky=(W, S, N, E))
    proba = ttk.Label(f2, text="kkkk")
    proba.grid(row=1, column=3, sticky=W)


kody = {"GSPPRB - Punkt Roboczy": GSPPRB, "Coś innego": COS}
pozyskania_lit = ("O", "A")
pozyskania_opis = ("pomiar na osnowę", "pomiar wykrywaczem przewodów")
pozyskania = ("O - pomiar na osnowę", "A - pomiar wykrywaczem przewodów")
blad_lp = ("1", "2", "3", "4", "5", "6")
blad_war = ("0.00 - 0.10", "0.11 - 0.30", "0.31 - 0.60", "0.61 - 1.50", "1.51 - 3.00", "powyżej 3.0")
blad = ("1 - 0.00 - 0.10", "2 - 0.11 - 0.30", "3 - 0.31 - 0.60", "4 - 0.61 - 1.50", "5 - 1.51 - 3.00", "6 - powyżej 3.0")


def pobierz(*args):
    global lp
    sciezka = filedialog.askopenfile().name
    plik = open(sciezka, "r")
    lista = plik.readlines()
    lista2 = list(map(lambda x: x.rstrip(), lista))
    lista2 = list(map(lambda x: x.lstrip(), lista2))
    lp = lista2
    listapunktow.set(value=lista2)
    otw_ety_txt.set(sciezka)
    zap_ety_txt.set(sciezka+".wsd")
    plik.close()
def test(*args):
    l = punkty.curselection()
    for i in l:
        print(lp[int(i)])
    f2.destroy()

def zapisz_sc(*args):
    sciezka = filedialog.asksaveasfile().name
    zap_ety_txt.set(sciezka+".wsd")
def co_wybr(*args):
    i = kod_obiektu_txt.get()
    kody[i]()

def gener(*args):
    global wyjscie
    typ = kod_obiektu_txt.get()
    if typ == "GSPPRB - Punkt Roboczy":
        wyjscie += "#Punkty inne=_code.n|_number|_X|_Y|_H|KRG.n|KRG.d|MPD.n|MPD.d|NSZ|DTP|BLP.n|BLP.d|_remarks\n"
    else:
        print("coś innego")
    l = punkty.curselection()
    wyb_pkt = list()
    for i in l:
        wyb_pkt.append(lp[int(i)])
    wyb_pkt = list(map(lambda x: x.replace(" ","|"),wyb_pkt))
    for i in wyb_pkt:
        wyjscie = wyjscie+"GSPPRB|"+i+"|"+krg_n_v.get()+"|"+krg_d_v.get()+"|"+mppd_nd_v.get().replace(" - ","|")+\
                  "|"+nsz_v.get()+"|"+dtp_v.get()+"|"+blp_nd_v.get().replace(" - ","|",1)+"|"+remarks_v.get()+"\n"
    f = open(zap_ety_txt.get(), "w")
    f.write(wyjscie)
    f.close()
    f2.destroy()

f = ttk.Frame(root)
f.grid(row=0, column=0, sticky=(W, S, N, E))

pplik_ety = ttk.Label(f, text="Ścieżka pliku wejściowego:", padding=5)
pplik_ety.grid(row=0, column=0, sticky=(W, S, N, E))

otw_ety = ttk.Label(f, textvariable=otw_ety_txt, relief="sunken", borderwidth=5, padding=5)
otw_ety.grid(row=1, column=0, sticky=(W, S, N, E))

otw = ttk.Button(f, command=pobierz, text="Importuj plik ze współrzędnymi.")
otw.grid(row=2, column=0, sticky=(W))

punkty = Listbox(f, height=15, listvariable=listapunktow, selectmode="extended")
punkty.grid(row=3, column=0, sticky=(W, S, N, E))

scroll_punkty = ttk.Scrollbar(f, orient=VERTICAL, command=punkty.yview)
scroll_punkty.grid(row=3, column=1, sticky=(N, S))
punkty.configure(yscrollcommand=scroll_punkty.set)

wplik_ety = ttk.Label(f, text="Ścieżka pliku wsadowego:", padding=5)
wplik_ety.grid(row=4, column=0, sticky=(W, S, N, E))

zap_ety = ttk.Label(f, textvariable=zap_ety_txt, relief="sunken", borderwidth=5, padding=5)
zap_ety.grid(row=5, column=0, sticky=(W, S, N, E))

zap = ttk.Button(f, command=zapisz_sc, text="Zmień plik zapisu.")
zap.grid(row=6, column=0, sticky=(W))

sep = ttk.Separator(f, orient=VERTICAL)
sep.grid(row=0, column=2, rowspan=7, sticky=(N, S))

kod_obiektu = ttk.Combobox(f, state="readonly", textvariable=kod_obiektu_txt)
kod_obiektu.grid(row=0, column=3, columnspan=3, sticky=(W, E))
kod_obiektu.configure(values=("GSPPRB - Punkt Roboczy","Coś innego"))
kod_obiektu.bind('<<ComboboxSelected>>', co_wybr)

f2 = ttk.Frame(f)
f2.grid(row=1, column=3, rowspan=6, sticky=(W, S, N, E))

klops = ttk.Button(f, command=test, text="test", padding=5)
klops.grid(row=7, column=0)


wyjscie = "#_SEPARATOR=|\n"





root.mainloop()
