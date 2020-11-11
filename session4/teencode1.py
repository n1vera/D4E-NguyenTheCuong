teencode = {
'lm': 'lam',
'hc': 'hoc',
'dc': 'duoc',
'cx': 'cung'
}
while True:
    for key in teencode:
        print(key, end=' '*10)
    print()
    print('*'*30)
    your_code = input('Your code?')
    if your_code in teencode:
        print(f'Trans {teencode[your_code]}')
    else:
        choice = input('Not found, want to add a new one ? (Y/N)')
        if choice == 'y':
            meaning = input('Enter your trans:')
            teencode[your_code] = meaning
        else :
            print('thanks')
            break
