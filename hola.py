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

    def ejecutar(self):
        print("=== Mi Calculadora V1.0 ===")
        while self.continuar:
            print("\nOperaciones disponibles:")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")

            opcion = input("\nSelecciona una operación (1-5): ")

            if opcion == "5":
                print("¡Hasta luego!")
                self.continuar = False
                break

            if opcion not in ["1", "2", "3", "4"]:
                print("Opción no válida")
                continue

            try:
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

                print(f"Resultado: {resultado}")
            except ValueError:
                print("Error: Debes ingresar números válidos")


if __name__ == "__main__":
    calc = Calculadora()
    calc.ejecutar()