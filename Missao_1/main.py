# Primeiro Desafio:
# Missão 1: Restaurando as Regras Escolares 📝
# O vírus apagou os critérios de aprovação dos alunos!
# Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado
# (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

nome_aluno = input("Digite o nome do aluno: ")
nota_aluno = float(input("Digite o nota aluno: "))

if nota_aluno >= 6:
    print(f"{nome_aluno}, você foi aprovado! Parabéns!")
else:
    print(f"{nome_aluno}, você foi reprovado, sentimos muito!")
