notas = [6, 7, 6.5, 4.8, 8]
soma = 0
for nota in notas:
    print(f"Nota: {nota}")
    soma += nota
media = sum(notas) / len(notas)
print(f"A média das notas é: {media:.2f}")