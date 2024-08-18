num = [1, 3, 6, 8, 10]
num.append(7)
num.sort()
num.sort(reverse=True)
num.remove(10)
print('Essa lista têm {} elementos!'.format(len(num)))
print(num)

a = [1, 2, 3]
b = a[:] # cópia dos valores de "a"
b[1] = 9
print('Lista A: {}'.format(a))
print('Lista B: {}'.format(b))

c = [4, 5, 6]
d = c # ligação entre essas duas listas
d[1] = 9
print('Lista C: {}'.format(c))
print('Lista D: {}'.format(d))
