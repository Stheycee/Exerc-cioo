p = ('detergente IPE 500 ML','Detergente em Pó Advanced 2,5 KG', 'Secante para lava louças Finish 250 ML','Omo 400 G')
print('-'*20)
print('Listagem de Produtos')
print('-'*20)
for i in range(0,len(p)):
    print(f'{p[i]}')
 
print(' ')   
print(f'O produto Omo aparece na posição {p.index("Omo 400 G")+1} da lista')
