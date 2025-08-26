# Sua solução aqui
altura = float(input())
sexo = input().strip().upper()

if sexo == "M":
    pesoideal = (72.7*altura)-58
elif sexo == "F":
   pesoideal = (62.1*altura)-44.7


print(f"peso_ideal:{pesoideal:.2f}")
