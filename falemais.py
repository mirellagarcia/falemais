#Produto FaleMais by: Mirella
print("Bem vindo ao FaleMais")

#Tabela de valores do DDD 
#011 - 016 R$1,90
#016 - 011 R$2,90
#011 - 017 R$1,70
#017 - 011 R$2,70
#011 - 018 R$0,90
#018 - 011 R$1,90 

ddd_origem = input("Qual DDD de origem? ")
ddd_destino = input("Qual DDD de destino? ")
calltime = int(input("Qual o tempo em minutos da ligação? "))
plano =  input("Você faz parte do plano FaleMais? Qual? ")

#FaleMais30 
if plano == "FaleMais30" and calltime <= 30:
  print("Seu plano é o FaleMais30 e não houve minutos excedidos")
##Calculo de minutos excedidos
elif plano == "FaleMais30" and calltime >= 31:
  print ("Seu plano é o FaleMais30 e a quantidade de minutos excedidos é de:")
excedido_30 = calltime - 30
if excedido_30 > 0 and plano == "FaleMais30":
    print(excedido_30, "minutos")


###Calculo do valor de minutos excedidos por DDD
if ddd_origem == "011" and ddd_destino == "016" and excedido_30 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_30 * (1.90 + (1.90*0.1)))
semplano = calltime * 1.90
if plano == "FaleMais30" and ddd_origem == "011" and ddd_destino == "016":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "016" and ddd_destino == "011" and excedido_30 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_30 * (2.90 + (2.90*0.1)))
semplano = calltime * 2.90
if plano == "FaleMais30" and ddd_origem == "016" and ddd_destino == "011":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)

if ddd_origem == "011" and ddd_destino == "017" and excedido_30 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_30 * (1.70 + (1.70*0.1)))
semplano = calltime * 1.70
if plano == "FaleMais30" and ddd_origem == "011" and ddd_destino == "017":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "017" and ddd_destino == "011" and excedido_30 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_30 * (2.70 + (2.70*0.1)))
semplano = calltime * 2.70
if plano == "FaleMais30" and ddd_origem == "017" and ddd_destino == "011":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "011" and ddd_destino == "018" and excedido_30 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_30 * (0.90 + (0.90*0.1)))
semplano = calltime * 0.90
if plano == "FaleMais30" and ddd_origem == "011" and ddd_destino == "018":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "018" and ddd_destino == "011" and excedido_30 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_30 * (1.90 + (1.90*0.1)))
semplano = calltime * 1.90
if plano == "FaleMais30" and ddd_origem == "018" and ddd_destino == "011":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)



#FaleMais60 
if plano == "FaleMais60" and calltime <= 60:
  print("Seu plano ideal é o FaleMais60 e não houve minutos excedidos")
##Calculo de minutos excedidos
elif plano == "FaleMais60" and calltime >= 61:
  print ("Seu plano é o FaleMais60 e a quantidade de minutos excedidos é de:")
excedido_60 = calltime - 60
if excedido_60 > 0 and plano == "FaleMais60":
    print(excedido_60, "minutos")


###Calculo do valor de minutos excedidos por DDD
if ddd_origem == "011" and ddd_destino == "016" and excedido_60 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_60 * (1.90 + (1.90*0.1)))
semplano = calltime * 1.90
if plano == "FaleMais60" and ddd_origem == "011" and ddd_destino == "016":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "016" and ddd_destino == "011" and excedido_60 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_60 * (2.90 + (2.90*0.1)))
semplano = calltime * 2.90
if plano == "FaleMais60" and ddd_origem == "016" and ddd_destino == "011":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "011" and ddd_destino == "017" and excedido_60 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_60 * (1.70 + (1.70*0.1)))
semplano = calltime * 1.70
if plano == "FaleMais60" and ddd_origem == "011" and ddd_destino == "017":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "017" and ddd_destino == "011" and excedido_60 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_60 * (2.70 + (2.70*0.1)))
semplano = calltime * 2.70
if plano == "FaleMais60" and ddd_origem == "017" and ddd_destino == "011":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "011" and ddd_destino == "018" and excedido_60 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_60 * (0.90 + (0.90*0.1)))
semplano = calltime * 0.90
if plano == "FaleMais60" and ddd_origem == "011" and ddd_destino == "018":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "018" and ddd_destino == "011" and excedido_60 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_60 * (1.90 + (1.90*0.1)))
semplano = calltime * 1.90
if plano == "FaleMais60" and ddd_origem == "018" and ddd_destino == "011":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


#FaleMais120 
if plano == "FaleMais120" and calltime <= 120:
  print("Seu plano ideal é o FaleMais120 e não houve minutos excedidos")
##Calculo de minutos excedidos
elif plano == "FaleMais120" and calltime >= 121:
  print ("Seu plano é o FaleMais120 e a quantidade de minutos excedidos é de:")
excedido_120 = calltime - 120
if excedido_120 > 0 and plano == "FaleMais120":
    print(excedido_120, "minutos")


###Calculo do valor de minutos excedidos por DDD
if ddd_origem == "011" and ddd_destino == "016" and excedido_120 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_120 * (1.90 + (1.90*0.1)))
semplano = calltime * 1.90
if plano == "FaleMais120" and ddd_origem == "011" and ddd_destino == "016":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "016" and ddd_destino == "011" and excedido_120 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_120 * (2.90 + (2.90*0.1)))
semplano = calltime * 2.90
if plano == "FaleMais120" and ddd_origem == "016" and ddd_destino == "011":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "011" and ddd_destino == "017" and excedido_120 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_120 * (1.70 + (1.70*0.1)))
semplano = calltime * 1.70
if plano == "FaleMais120" and ddd_origem == "011" and ddd_destino == "017":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "017" and ddd_destino == "011" and excedido_120 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_120 * (2.70 + (2.70*0.1)))
semplano = calltime * 2.70
if plano == "FaleMais120" and ddd_origem == "017" and ddd_destino == "011":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "011" and ddd_destino == "018" and excedido_120 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_120 * (0.90 + (0.90*0.1)))
semplano = calltime * 0.90
if plano == "FaleMais120" and ddd_origem == "011" and ddd_destino == "018":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)


if ddd_origem == "018" and ddd_destino == "011" and excedido_120 > 0:
  print("O valor da fatura com o plano FaleMais é de: ", excedido_120 * (1.90 + (1.90*0.1)))
semplano = calltime * 1.90
if plano == "FaleMais120" and ddd_origem == "018" and ddd_destino == "011":
 print("O valor da sua fatura sem o plano FaleMais é de: ",semplano)
