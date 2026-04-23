contador = 0
perguntas = [
"1- Telefonou para a vítima? (s/n) ", 
"2- Esteve no local do crime? (s/n) ", 
"3- Mora perto da vítima? (s/n) ", 
"4- Devia para a vítima? (s/n) ", 
"5- Já trabalhou com a vítima? (s/n) "
]

for pergunta in perguntas:
    resp = input(pergunta)
    if resp == "s":
        contador += 1
    
if contador == 2:
    print("Suspeita")
elif contador == 3 or contador == 4:
    print("Cúmplice")
elif contador == 5:
    print("Assassino")
else:
    print("Inocente")