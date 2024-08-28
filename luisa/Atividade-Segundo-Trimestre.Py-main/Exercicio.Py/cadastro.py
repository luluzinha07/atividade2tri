class Cadastro:
    def __init__(self,nome,idade,sexo,email,telefone,endereco):
        self.nome = nome 
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
     return f'Seu nome:{self.nome}  Sua idade:{self.idade}  Seu sexo:{self.sexo}  Seu email:{self.email}  Seu telefone:{self.telefone}   Seu endereco:{self.endereco}'
 
cad1 = Cadastro ('Matheus',17,'masc','Matheussantos@gmail.com','41 4321 1234','rua 15')

print (cad1)