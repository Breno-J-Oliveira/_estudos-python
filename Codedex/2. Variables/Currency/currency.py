# Write code below 💖

peso = int(input("What do you have left in pesos? "))

#1 peso é igual a 0.00068 dolares

soles = int(input("What do you have left in soles? "))

#1 soles é igual a 0.29

reais = int(input("What do you have left in reais? "))

#1 real é igual a 0.20 dolares

conver_peso = peso * 0.00068
conver_soles = soles * 0.29
conver_reais = reais * 0.20

dolar = conver_peso + conver_soles + conver_reais

print(dolar)
