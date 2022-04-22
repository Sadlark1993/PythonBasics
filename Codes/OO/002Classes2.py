
class Circulos:
    raio = 25.4
    def calculaArea(self):
        self.area = 3.14*(self.raio**2)
    def calculaVolume(self, altura):
        self.volume = 3.14*(self.raio**2)*altura

c1 = Circulos()

c1.calculaArea()
print(c1.area)
c1.calculaVolume(12.)
print(c1.volume)
