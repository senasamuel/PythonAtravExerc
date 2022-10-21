#Entrada de dados 
input("Vamos informar  3 número e informar  qual é o maior.")
A = input(" Informe o 1° números:").split()
B = input(" Informe o 2° números:").split()
C = input(" Informe o 3° números:").split()

#Processamento
ganhador = None 
if A != B and A != C:
    ganhador = ' O ganhador foi A'
elif B != A and B != C:
     ganhador = 'O ganhador foi B'    
elif C != A and C != B:
     ganhador = 'O ganhador foi C'
else:
     ganhador = 'impate '    

#Saída
print("O ganhador foi ",ganhador)           