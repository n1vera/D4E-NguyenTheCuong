teencode = {
'lm': 'lam',
'hc': 'hoc',
'dc': 'duoc',
'cx': 'cung'
}
print(teencode, end='                ')
print('***********************************************************************')
for key in teencode:
    a = input('Your code?')
    if a == key:
        print(f'Trans {teencode[a]}')


# else:
#     print('ban co muon them vao tu dien?')
#     input('Y/N')
#     if input == 'Y':
