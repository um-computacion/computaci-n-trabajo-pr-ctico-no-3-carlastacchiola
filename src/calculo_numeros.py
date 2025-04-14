try: 
    from .exceptions import NumeroDebeSerPositivo
except ImportError:
    from exceptions import  NumeroDebeSerPositivo

def ingrese_numero():
    try:
        entrada = input("Ingrese un número: ")
        numero = int(entrada)
        if numero <= 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo.")
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido.")

if __name__ == "__main__":
    try:
        numero = ingrese_numero()
        print(f"Número válido: {numero}")
    except NumeroDebeSerPositivo as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario (Ctrl+C)")


