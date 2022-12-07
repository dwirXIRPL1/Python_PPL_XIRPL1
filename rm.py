class Agama:
    def __init__(self, nama, agama):
        self.nama = nama
        self.agama = agama

    def perkenalan(self):
        print(self.nama, "Beragama", self.agama)

class Islam(Agama):
    def __init__(self, nama, agama, solat):
        Agama.__init__(self, nama, agama)
        self.solat = solat

class Budha(Agama): 
    def __init__(self, nama, agama, sembahyang):
        Agama.__init__(self, nama, agama)
        self.sembahyang = sembahyang

rama = Islam('Rama', 'Islam', 'Solat')  
rama.perkenalan()
print(f'{rama.nama} beribadah dengan melakukan {rama.solat}')

abraham = Budha('Abraham', 'Krister', 'Sembahyang')  
abraham.perkenalan()
print(f'{abraham.nama} beribadah dengan melakukan {abraham.sembahyang}')