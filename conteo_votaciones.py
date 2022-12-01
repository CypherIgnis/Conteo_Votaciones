class Votations():

    def __init__(self):
        print("Comenzando programa")
        self.__candidate=candidate
        self.__party=party
        self.__counting=counting
        
    def get__candidate(self):
        return self.__candidate
    
    def set__candidate(self,value):
        self.__candidate = value
    
    def get__party(self):
        return self.__party
    
    def set__party(self,value):
        self.__party = value
    
    def get__counting(self):
        return self.__counting
    
    def set__counting(self,value):
        self.__counting = value

    def show_candidate(self):
        print(self.candidato)

    def show_party(self):
        print(self.partido)

    def show_counting(self):
        print(self.conteo)
        
    def candidate(self,candidato):
        return self.candidato
     
    def party(self,partido):
        return self.partido
        
    def counting(self,conteo):
        return self.conteo
      
a=candidate("Piñera")
print(a.candidato)

