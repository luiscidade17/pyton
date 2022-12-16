class Pessoa:
    def __init__(self):
        self.nome=""
        self.idade=0
        self.sexo=""
    
    def set_sexo(self, sexo):
        self.sexo = sexo
        
    def set_nome(self, nome):
        self.nome = nome
        
    def set_idade(self, idade):
        self.idade = idade
    
    def get_nome(self):
        return self.nome
        
