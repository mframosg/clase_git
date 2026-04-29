import math

class Calculadora:
    def __init__(self):
        self.continuar = True

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por cero"
        return a / b

    def modulo(self, a, b):
        if b == 0:
            return "Error: No se puede calcular módulo con cero"
        return a % b

    def potencia(self, a, b):
        return a ** b

    def raiz_cuadrada(self, a):
        if a < 0:
            return "Error: No se puede calcular raíz de número negativo"
        return math.sqrt(a)

    def porcentaje(self, a, b):
        return (a * b) / 100

    def seno(self, a):
        return math.sin(math.radians(a))

    def coseno(self, a):
        return math.cos(math.radians(a))

    def tangente(self, a):
        return math.tan(math.radians(a))

    def logaritmo(self, a):
        if a <= 0:
            return "Error: El logaritmo debe ser de un número positivo"
        return math.log10(a)

    def logaritmo_natural(self, a):
        if a <= 0:
            return "Error: El logaritmo debe ser de un número positivo"
        return math.log(a)

    def valor_absoluto(self, a):
        return abs(a)

    def ejecutar(self):
        print("=== Calculadora Avanzada ===")
        while self.continuar:
            print("\n" + "="*40)
            print("OPERACIONES DISPONIBLES:")
            print("="*40)
            print("BÁSICAS:")
            print("  1. Sumar")
            print("  2. Restar")
            print("  3. Multiplicar")
            print("  4. Dividir")
            print("  5. Módulo (residuo)")
            print("\nPOTENCIA Y RAÍZ:")
            print("  6. Potencia (a^b)")
            print("  7. Raíz cuadrada")
            print("\nPORCENTAJE:")
            print("  8. Calcular porcentaje")
            print("\nTRIGONOMETRÍA:")
            print("  9. Seno")
            print("  10. Coseno")
            print("  11. Tangente")
            print("\nLOGARITMOS:")
            print("  12. Logaritmo base 10")
            print("  13. Logaritmo natural")
            print("\nOTRAS:")
            print("  14. Valor absoluto")
            print("  15. Salir")
            print("="*40)

            opcion = input("\nSelecciona una operación (1-15): ")

            if opcion == "15":
                print("\n¡Hasta luego!")
                self.continuar = False
                break

            try:
                if opcion in ["1", "2", "3", "4", "5", "6", "8"]:
                    num1 = float(input("Ingresa el primer número: "))
                    num2 = float(input("Ingresa el segundo número: "))

                    if opcion == "1":
                        resultado = self.sumar(num1, num2)
                    elif opcion == "2":
                        resultado = self.restar(num1, num2)
                    elif opcion == "3":
                        resultado = self.multiplicar(num1, num2)
                    elif opcion == "4":
                        resultado = self.dividir(num1, num2)
                    elif opcion == "5":
                        resultado = self.modulo(num1, num2)
                    elif opcion == "6":
                        resultado = self.potencia(num1, num2)
                    elif opcion == "8":
                        resultado = self.porcentaje(num1, num2)

                elif opcion in ["7", "9", "10", "11", "12", "13", "14"]:
                    num1 = float(input("Ingresa el número: "))

                    if opcion == "7":
                        resultado = self.raiz_cuadrada(num1)
                    elif opcion == "9":
                        resultado = self.seno(num1)
                    elif opcion == "10":
                        resultado = self.coseno(num1)
                    elif opcion == "11":
                        resultado = self.tangente(num1)
                    elif opcion == "12":
                        resultado = self.logaritmo(num1)
                    elif opcion == "13":
                        resultado = self.logaritmo_natural(num1)
                    elif opcion == "14":
                        resultado = self.valor_absoluto(num1)
                else:
                    print("Opción no válida")
                    continue

                print(f"\n✓ Resultado: {resultado}")
            except ValueError:
                print("Error: Debes ingresar números válidos")


if __name__ == "__main__":
    calc = Calculadora()
    calc.ejecutar()