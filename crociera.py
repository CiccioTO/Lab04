
class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO

        self._nome = nome
        self.cabine=[]
        self.persone=[]
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    def __str__(self):
        return f" 'Nome crociera': {self._nome} "

    """Aggiungere setter e getter se necessari"""

    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line=line.strip().split(',')
                if len(line) == 4:
                    codicecab=line[0]
                    posti_letto=int(line[1])
                    ponte=int(line[2])
                    prezzo=float(line[3])
                    disponibile = True
                    cabina=Cabina(codicecab,posti_letto,ponte,prezzo,disponibile)
                    self.cabine.append(cabina)
                elif len(line) == 5:
                    if line[4].isalpha():
                        codicecab=line[0]
                        posti_letto=int(line[1])
                        ponte=int(line[2])
                        prezzo=float(line[3])
                        tipologia=line[4]
                        disponibile=True
                        cabina=CabinaDeluxe(codicecab,posti_letto,ponte,prezzo,disponibile,tipologia)
                        self.cabine.append(cabina)
                    elif line[4].isdigit():
                        codicecab=line[0]
                        posti_letto=int(line[1])
                        ponte=int(line[2])
                        prezzo=float(line[3])
                        num_animali=float(line[4])
                        disponibile = True
                        cabina=CabinaAnimali(codicecab,posti_letto,ponte,prezzo,disponibile,num_animali)
                        self.cabine.append(cabina)
                elif len(line) == 3:
                    codicepas=line[0]
                    nome=line[1]
                    cognome=line[2]
                    alloggiato=False
                    passeggero=Passeggero(codicepas,nome,cognome,alloggiato,cabina='il passeggero non ha nessuna cabina assegnata')
                    self.persone.append(passeggero)
    def assegna_passeggero_a_cabina(self, codice_cabina,codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        for cabina in self.cabine:
            if cabina.codicecab == codice_cabina:
                for passeggero in self.persone:
                    if passeggero.codpas == codice_passeggero:
                        if cabina.disponibile==True and passeggero.alloggiato==False:
                            cabina.disponibile = False
                            passeggero.alloggiato = True
                            passeggero.cabina=f'{cabina.codicecab}'
                            return "Cabina assegnata con successo."
                        else:
                            return "Cabina assegnata non con successo."
    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO

        lista_ordinata=sorted(self.cabine, key=lambda x: x.prezzo)
        return lista_ordinata


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for passeggero in self.persone:
            print(passeggero)





class Cabina:
    def __init__(self, codicecab,posti_letto,ponte,prezzo,disponibile):
        self.codicecab = codicecab
        self.posti_letto = posti_letto
        self.ponte = ponte
        self.prezzo = prezzo
        self.disponibile = True
    def __str__(self):
        return f"'Codice cabina:' {self.codicecab} ' posti letto:' {self.posti_letto} 'numero ponte:' {self.ponte} 'prezzo:' {self.prezzo}"

class CabinaDeluxe(Cabina):
    def __init__(self, codicecab,posti_letto,ponte,prezzo,disponibile,tipologia):
        super().__init__(codicecab, posti_letto, ponte, prezzo,disponibile)
        self.tipologia = tipologia
        self.prezzo = prezzo * 1.20
    def __str__(self):
        return f" 'Codice cabina:' {self.codicecab} 'posti letto:' {self.posti_letto} 'numero ponte: '{self.ponte} 'prezzo:' {self.prezzo} 'tipologia:' {self.tipologia}"

class CabinaAnimali(Cabina):
    def __init__(self, codicecab,posti_letto,ponte,prezzo,disponibile,num_animali):
        super().__init__(codicecab,posti_letto,ponte,prezzo,disponibile)
        self.num_animali = num_animali
        self.prezzo = prezzo *(1+0.10*num_animali)
    def __str__(self):
        return f" 'Codice cabina:' {self.codicecab} 'posti letto:' {self.posti_letto} 'numero ponte: '{self.ponte} 'prezzo:' {self.prezzo} 'numero animali:' {self.num_animali}"
class Passeggero:
    def __init__(self, codpas,nome,cognome,alloggiato,cabina):
        self.codpas = codpas
        self.nome = nome
        self.cognome = cognome
        self.alloggiato = False
        self.cabina = 'il passeggero non ha nessuna cabina assegnata'
    def __str__(self):
        return f" 'Codice passegero:' {self.codpas} 'nome:' {self.nome} 'cognome:' {self.cognome} 'Codice cabina:' {self.cabina}"








