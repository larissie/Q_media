Name = input("Digite seu nome:")
print ("Olá,",Name)
print ("Seja bem-vindo á calculadora de média do Q-acadêmico")
AV1N1 = float(input("Digite sua nota da AV1N1:"))
AV2N1 = float(input("Digite sua nota da AV2N1:"))
N1 = (AV1N1 + AV2N1)/2
print ("Sua média da N1 foi:",N1)
AV1N2 = float(input("Digite sua nota da AV1N2:"))
AV2N2 = float(input("Digite sua nota da AV2N2:"))
N2 = (AV1N2 + AV2N2)/2
print ("Sua média da N2 foi:",N2)
MP = (N1 *2 + N2*3)/5
print ("Sua média parcial foi:", MP)
if (MP>5.9):
  print("VOCÊ FOI APROVADO")
else: print("PROVA FINAL")
PF = float(input("Informe sua nota na PF. Se aprovado, digite sua média parcial:"))
MF = (PF + MP)/2
print("Sua média final foi:",MF)
if (MF>4.9):
  print("Parabéns",Name)
  print("VOCÊ FOI APROVADO")
else:
  print("Sinto muito",Name)
  print("VOCÊ FOI REPROVADO")