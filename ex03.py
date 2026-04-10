class Calculadora: 
    def adicionar(self, a, b):
        return a+b
    def subtrair(self, a, b):
        return a-b
    def dividir(self, a, b):
        if a == 0 and b == 0:
            return "Divisão por zero não é permitida."
        return a/b
    def multiplicar(self, a, b):
        if a == 0 or b == 0:
            return "Multiplicação por zero não é permitida."
        return a*b
    
calc = Calculadora()
print(calc.subtrair(3,1))
print(calc.multiplicar(3,0))