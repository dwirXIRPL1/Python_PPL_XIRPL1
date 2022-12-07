class siswa :
    def __init__(self, murid):
        self.murid = murid;

murid_kami = siswa('euroski')

print(f'1.murid kami bernama {murid_kami.murid} ganteng\n ')

class guru:
    def __init__(self, guru):
        self._guru = guru

class guruku(guru):
    def __init__(self, guru, penampilan):
        super().__init__(guru)
        self._penampilan = penampilan

    def pamer(self):
        print(f'2.guru kami bernama {self._guru} yang {self._penampilan}\n')

guru = guruku('bu anita', 'cantik')
guru.pamer() 

class kepsek:
    def __init__(self, kepalasekolah):
        self._kepalasekolah = kepalasekolah

    def nama_kepsek (self):
        print(f'3.kepsek kami bernama {self._kepalasekolah}')

kepsek = kepsek('pak lilik')
kepsek.nama_kepsek()