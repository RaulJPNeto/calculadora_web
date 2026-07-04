class Calculadora:
    def somar(self, a: float, b: float) -> float:
        return a + b

    def subtrair(self, a: float, b: float) -> float:
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        return a * b

    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b


OPERACOES = {
    "+": Calculadora.somar,
    "-": Calculadora.subtrair,
    "*": Calculadora.multiplicar,
    "/": Calculadora.dividir,
}
