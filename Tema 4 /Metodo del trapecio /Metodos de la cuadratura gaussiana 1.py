# Método del trapecio

# Concepto:
# Este método se basa en la aproximación del área bajo la curva mediante trapecios. 
# Divide el área bajo la curva en varios trapecios y luego -
# calcula la suma de las áreas de estos trapecios para aproximar la integral definida.

#Fórmula: 
    # [(DeltaX o H]* [f(a)+f(b)]/2 para solo una interaccion

# Significado de la simbología:

#    - f(x0): Funcion evaluada con intervalo a.
#    - f(x1,x2): Funciom evaludada con n.
#    - ( DeltaX o h): Funcion evaluada (b-a)/n
#    - ( a ) y ( b ): Extremos del intervalo de integración.

String = "f(x) = ∫x^3+6x^2+11x-6 dx  en los puntos a:1.3   &   b: 1.8"

# 1) Definir ecuacion
def f(x):
    return x**3 + 6*x**2 + 11*x - 6

# 2) Definir puntos a y b
a , b = 1.3, 1.8

# 3) Implementacion de la formula

# 3.1) realizar la diferencia de b-a
def deltax():
    return b - a
# 3.2) Realizar la suma de las funciones evaluadas en punto "a" y "b" y enseguida dividirlas entre 2
def Suma():
    return (f(a) + f(b)) / 2

def metodoResultado():
    H = deltax()
    S = Suma()
    return H * S

# Calcular el resultado
mR = metodoResultado()

#Calcular el margen de error

def margenError():
    error = 14.705395
    return abs ((error - mR)/error)*100

# Calcular margen de error
mE = margenError()

# Resultados
print("")
print("La ecuación ingresada es: ", String)
print("El parámetro a o límite inferior es: ", a)
print("El parámetro b o límite superior es: ", b)
print("El resultado aplicando el método del trapecio es:", mR)
print("Bibliografía:https://es.symbolab.com/solver/step-by-step/%5Cint_%7B1.3%7D%5E%7B1.8%7D%20x%5E%7B3%7D%2B6x%5E%7B2%7D%2B11x-6dx?or=input")
print("El link anterior demuestra el resultado en Symbolab para confirmar la validez del resultado")
print("El margen de error es: ",mE)
print("")
