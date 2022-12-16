from myalunos import Aluno

alunoA = Aluno (18, "Luis")
alunoB = Aluno (22, "José Pantera")

#Variável Idade 
tmp=alunoA.idade

#Troca de idades pelos alunos
alunoA.idade = alunoB.idade
alunoB.idade = tmp

print(alunoA.idade)
print(alunoB.idade)
