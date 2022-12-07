class Agama:
    def __init__(self, nama, agama):
        self.nama = nama
        self.agama = agama
    
    def perkenalan(self):
        print(self.nama, "Beragama", self.agama )

class Islam(Agama):
    def __init__(self, nama, agama, sholat):
        Agama.__init__(self, nama, agama)
        self.sholat = sholat

class Budha(Agama):
    def __init__(self, nama, agama, sembahyang):
        Agama.__init__(self, nama, agama)
        self.sembahyang = sembahyang

hisyam = Islam('Hisyam', 'Islam', 'Sholat')
hisyam.perkenalan()
print(f'{hisyam.nama} beribadah dengan melakukan {hisyam.sholat}')

abraham = Budha('Abraham', 'Budha', 'Sembahyang')
abraham.perkenalan()
print(f'{abraham.nama} beribadah dengan melakukan{abraham.sembahyang}')