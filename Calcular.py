aluno = input('Nome do aluno(a): ')
nota1 = input('Primeira nota: ')
nota2 = input('Segunda nota: ')
nota3 = input('Terceira nota: ')

resultado1 = int(nota1)
resultado2 = int(nota2)
resultado3 = int(nota3)

soma = resultado1 + resultado2 + resultado3
media = soma / 3

print(aluno, f'teve média de {media:.2f}')

if media >= 7:
  print(aluno, 'foi aprovado(a)!')
else:
  print(aluno, 'foi reprovado(a) :(')
