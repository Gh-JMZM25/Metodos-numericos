import math
def funcion(x):
    return math.exp(-x**2)
def cuadratura_gaussiana(a, b, n):
    coeficientes = {2: [1.0, 1.0], 
                    3: [0.5555555556, 0.8888888889, 0.5555555556], 
                    4: [0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451], 
                    5: [0.2369268851, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268851], 
                    6: [0.1713244924, 0.3607615730, 0.4679139346, 0.4679139346, 0.3607615730, 0.1713244924]}
    nodos = {2: [-0.5773502692, 0.5773502692], 
             3: [0.0, -0.7745966692, 0.7745966692],
             4: [-0.3399810436, 0.3399810436, -0.8611363116, 0.8611363116], 
             5: [0.0, -0.5384693101, 0.5384693101, -0.9061798459, 0.9061798459], 
             6: [0.6612093865, -0.6612093865, -0.2386191861, 0.2386191861, -0.9324695142, 0.9324695142]}
    suma = 0
    for i in range(n):
        xi = ((b - a) * nodos[n][i] + a + b) / 2
        suma += coeficientes[n][i] * funcion(xi)
    return (b - a) / 2 * suma
limite_inferior = 0
limite_superior = 1
numero_puntos_gauss = 4
resultado_integral = cuadratura_gaussiana(limite_inferior, limite_superior, numero_puntos_gauss)
print("El resultado de la integral es:", resultado_integral) 
