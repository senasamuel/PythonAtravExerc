#Entrada de dados 

A , B = input("Informe as duas notas :").split()


A = float(A)
B = float(B)

#Processamento 
media = (A + B) / 2
resposta = ''

if media >= 7:
    resposta = 'Aprovado'
elif media < 7 and media >= 4:
    resposta = 'Recuperação'    
else:
    resposta = 'Reprovado'

#Saída 
    
print(resposta)    
