alunos = []
n = int(input("Digite o número de alunos: "))
for i in range(n):
    nome = input(f"Digite o nome do {i+1}º aluno: ").capitalize()
    nota = float(input(f"Digite a nota do aluno {nome}: "))
    alunos.append((nome, nota))
print(alunos)
media = sum(nota for nome, nota in alunos) / len(alunos)    
print(f"A média das notas é: {media:.2f}")

for nome, nota in alunos:
    if nota > media:
        print(f"O aluno {nome} tem a nota {nota:.2f} e está acima da média, Parabéns!")


while True:
    n = int(input("Digite o índice do aluno: "))
    if n>=0 and n< len(alunos): break
    else:print("Índice inválido. Tente novamente.")
    
print(f"O aluno {alunos[n][0]} tem a nota {alunos[n][1]:.2f}")

nome = input("Digite o nome do aluno: ")
if nome in [aluno[0] for aluno in alunos]:
    index = next(i for i, aluno in enumerate(alunos) if aluno[0] == nome)
    print(f"A média da turma é {media:.2f}O aluno {nome} tem a nota {alunos[index][1]:.2f} e está acima da média, Parabéns!")
else:print("Aluno não encontrado")