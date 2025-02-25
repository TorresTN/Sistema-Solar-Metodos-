class CalculosGravitacionales:
    def __init__(self):
        # Constante gravitacional universal
        self.G = 6.67430e-11  # m³ kg^-1 s^-2
        # Masa del Sol (fija)
        self.masa_Sol = 1.989e30  # kg

    def fuerza_gravitacional(self, masa_planeta, distancia):
        """
        Calcula la fuerza gravitacional entre el Sol y un planeta.
        
        Parámetros:
        masa_planeta (float): Masa del planeta en kg
        distancia (float): Distancia entre el Sol y el planeta en metros
        
        Retorna:
        float: Fuerza gravitacional en Newtons
        """
        try:
            # Verificar valores positivos
            if masa_planeta <= 0 or distancia <= 0:
                raise ValueError("La masa y la distancia deben ser valores positivos")
            
            # Calcular la fuerza gravitacional
            fuerza = self.G * (self.masa_Sol * masa_planeta) / (distancia ** 2)
            return fuerza
        
        except ValueError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

    def calcular_aceleracion(self, fuerza, masa):
        """
        Calcula la aceleración usando la Segunda Ley de Newton.
        
        Parámetros:
        fuerza (float): Fuerza gravitacional en Newtons
        masa (float): Masa del planeta en kg
        
        Retorna:
        float: Aceleración en m/s²
        """
        try:
            if masa <= 0:
                raise ValueError("La masa debe ser un valor positivo")
            return fuerza / masa
        except ValueError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

# Ejemplo de uso
if __name__ == "__main__":
    calc = CalculosGravitacionales()
    
    try:
        # Solicitar datos al usuario
        print("\nCalculadora de Fuerza Gravitacional y Aceleración")
        print("===============================================")
        masa_planeta = float(input("Ingrese la masa del planeta en kg (ejemplo: 5.972e24): "))
        distancia = float(input("Ingrese la distancia al Sol en metros (ejemplo: 1.496e11): "))
        
        fuerza = calc.fuerza_gravitacional(masa_planeta, distancia)
        
        if fuerza is not None:
            print(f"\nResultados:")
            print(f"La fuerza gravitacional entre el Sol y el planeta es: {fuerza:.2e} Newtons")
            
            # Calcular y mostrar la aceleración
            aceleracion = calc.calcular_aceleracion(fuerza, masa_planeta)
            if aceleracion is not None:
                print(f"La aceleración gravitacional del planeta es: {aceleracion:.10f} m/s²")
            
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos")