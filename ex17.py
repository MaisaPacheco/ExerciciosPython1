#17) Desafio ex17.py: Dada uma equação de segundo grau, calcule suas raízes utilizando a fórmula de Bhaskara.

a=input('coeficiente a')
b=input('coeficiente b')
c=input('coeficiente c')

delta=float(b)**2-4*float(a)*float(c)
print(delta)
x1=(-float(b)+delta**0.5)/2
print(x1)
x2=(-float(b)-delta**0.5)/2
print (x2)