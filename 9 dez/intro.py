#DEFINIR A VARIÁVEL (Nome e Idade)
nome1 = "luis" 
nome2 = "Cidade"


idade1 = 18
idade2 = 18

#Nome
print(nome1+" "+nome2)
# Soma das idades 
print(idade1+idade2)

#Valor constante
#O NOME DA VARIÁVEL FICA SEMPRE EM MAIUSCULAS
ID = 10
print(ID)

#METODO DE METER A PRIMEIRA LETRA EM MAIUSCULO
print(nome1.capitalize())

#METODO DE METER A PALAVRA TODA EM MAIUSCULO
print(nome1.upper())

#METODO DE PERGUNTAR SE A FRASE ESTÁ TODA EM MINÚSCULO
print(nome1.islower())


#Listagem das letras no nome
print (nome1[0])
print (nome1[1])
print (nome1[2])
print (nome1[3])

#Listagem das letras no nome com restrição

print (nome1[:2]) #Com os pontos antes do numero, retribui as letras antes do caractere 2
print (nome1[2:]) #Com os pontos depois do numero, retribui as letras DEPOIS do caractere 2
