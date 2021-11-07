c = int(input('Digite um número de 1 a 100:'))
n = 0
for d in range(1, 101):
    if c % d == 0:
        n = n + 1

if n == 2:
    print("É número primo")
else:
    print("Não é número primo")