"""
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.
"""
char = input('Digite algo: ')

print('Tipo primitivo: {}!'.format(type(char)))
print('Pode ser convertido para númerico? {}'.format('Sim' if char.isnumeric() else 'Não'))
print('Todas as letras maiúscula? {}'.format('Sim' if char.isupper() else 'Não'))
print('O tamanho da informação é de {}!'.format(len(char)))
