num = int(input('Digite um número: '))

print(f'{" Tabuada de {} ":=^30}'.format(num))
for c in range(1, 11):
    print('{} *  {} = {}'.format(num, c, num * c))
# referente à aula 13
