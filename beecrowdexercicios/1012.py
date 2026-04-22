n1, n2, n3 = map(float, input().split())
pi = 3.14159
triangulo = n1 * n3 / 2
circulo = n3 ** 2 * pi
trapezio = (n1 + n2) / 2 * n3
quadrado = n2 ** 2
retangulo = n1 * n2
print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')