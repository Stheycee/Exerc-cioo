loc = list()
dici = {'nome': 'Mar em fúria', 'Gênero': 'Ação', 'Valor por 24h': 'R$ 12,00'}
dici1 = {'nome': 'Duelo de Titãs', 'Gênero': 'Drama', 'Valor por 24h': 'R$ 10,00'}
dici2 = {'nome': 'A corrente do bem', 'Gênero': 'Romance', 'Valor por 24h': 'R$ 13,00'}
dici3 = {'nome': 'Homens de honra', 'Gênero': 'Drama', 'Valor por 24h': 'R$ 12,00'}
dici4 = {'nome': 'A nova onda do imperador', 'Gênero': 'Comédia', 'Valor por 24h': 'R$ 12,00'}
loc.append(dici)
loc.append(dici1)
loc.append(dici2)
loc.append(dici3)
loc.append(dici4)


for e in loc:
    for k,v in e.items():
        print(f'O {k} é {v}')
    print(' ')
        


