Regras = "Bem Vindo- PRESSIONAR ENTER PARA COMEÇAR "
Introcução_Jogo = "TIIGR2-GAME Cabeçudos."
Pistas = "Todos os nomes VÁLIDOS, SÃO DE COLEGAS DE TURMA"
Opções = "Jose / Miguel / Paulo / Henrique / Paulo Leite"

print(input(Regras))
print(input (Introcução_Jogo))
print(input(Pistas))
print (input(Opções))

Palavras_Acertadas = []

while len(Palavras_Acertadas) < 3:
  print("Tentativas {}".format(len(Palavras_Acertadas)))

  player = (input('Quem tem a maior Cabeça da Turma?:'))

  if player == 'Jose':
    print('Não tem a Maior Cabeça. mas está quase.')

    if 'Jose' not in Palavras_Acertadas:
      Palavras_Acertadas.append('Jose')

  elif player == 'Paulo' :
    print('Muito Longe')

    if 'Paulo' not in Palavras_Acertadas:
      Palavras_Acertadas.append('Paulo')
  elif player == 'Miguel':
    print('ACERTOU MACACOO, AS TUAS CAPACIDADES EM TÉCNICO TÁ DO CARAÇAS!')

    if 'Miguel' not in Palavras_Acertadas:
      Palavras_Acertadas.append('Miguel')
    if player == 'Jose':
     print('Não tem a Maior Cabeça. mas está quase.')

    
    if 'Jose' not in Palavras_Acertadas:
      Palavras_Acertadas.append('Jose')

  elif player == 'Paulo' :
    print('Muito Longe')

    if 'Paulo' not in Palavras_Acertadas:
      Palavras_Acertadas.append('Paulo')
      
  elif player == 'Miguel':
    print('ACERTOU MACACOO, AS TUAS CAPACIDADES EM TÉCNICO TÁ DO CARAÇAS!')

    if 'Miguel' not in Palavras_Acertadas:
      Palavras_Acertadas.append('Miguel')  
      
  elif player == 'Paulo Leite':
    print('NÃO É ALUNO, TENTA MAIS TARDE !')      
      

print("Terminou")
