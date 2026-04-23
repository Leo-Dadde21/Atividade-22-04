nomes = []

x = int(input("Digite o número de alunos: "))
for i in range(x):
    n = input(f"Digite o nome do {i+1}º aluno: ").capitalize()
    nomes.append(n)
   
for i, nome in enumerate(nomes):
    print(f"{i} - {nome}")