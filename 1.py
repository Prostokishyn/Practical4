class Drib:
    def __init__(self, chiselnik, znamennik):
        self.chiselnik = chiselnik
        self.znamennik = znamennik
    
    def drib_correct(self):
        if self.chiselnik < self.znamennik:
            return True
        else:
            return False
        
drib1 = Drib(2, 3)
drib2 = Drib(5, 2)
print(drib1.drib_correct())
print(drib2.drib_correct())