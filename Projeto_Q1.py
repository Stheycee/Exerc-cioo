dici = list()
info = list()  
notas = list()  

while True:
    info.append(str(input('\nDisciplina: ').title()))
    notas.append(float(input('1ª Nota : ')))
    notas.append(float(input('2ª Nota : ')))
    info.append(notas[:])
    info.append((notas[0] + notas[1]) / 2)
    dici.append(info[:])
    
    info.clear()
    notas.clear()

    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? S/N ')).upper().strip()[0]
        if r not in 'SN':
            print('Digite apenas "S" para não e "N" para não.')
    if r == 'N':
        break


print(f'\n{"=-=" * 10}\n{"Disciplinas:        Média:"}')
for i, aluno in enumerate(dici):
    print(f'{aluno[0]:^7}  {aluno[2]:>9.1f}')
print(f'{"=-=" * 10}')


