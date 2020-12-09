carteiras= []
car=[]
tei=[]
ras=[]
tipoA = {'nome': 'Joana','Aluno': 'José'}
tipoB = {'nome': 'Maria','Aluno': 'Tereza','estudante':'Paulo','Nome':'Bruna'}
tipoAB = {'nome': 'João','aluno':'Beatriz'}
tipoC = {'nome':'Pedro'}
carteiras.append(tipoA)
car.append(tipoB)
tei.append(tipoAB)
ras.append(tipoC)


for a in carteiras:
    for k,v in a.items():
        print(f'O {k} é {v}, qualificado(a) para o Tipo A')
    print(' ')

for e in car:
    for b,c in e.items():
        print(f'O {b} é {c}, qualificado(a) para o Tipo B')
    print(' ')

for i in tei:
    for d,f in i.items():
        print(f'O {d} é {f}, qualificado(a) para o Tipo AB')
    print(' ')

for o in ras:
    for g,h in o.items():
        print(f'O {g} é {h}, qualificado(a) para o Tipo C')
    print(' ')
