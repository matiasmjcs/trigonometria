import math 
# ejercicio 1
hipotenusa_01: int = 36
angulo_alfa_01: int = 28
valor_en_radianes_01: float = math.radians(angulo_alfa_01)
cateto_opuesto_01: float = hipotenusa_01 * math.sin(valor_en_radianes_01)
print(cateto_opuesto_01)
# ejercicio 2 
angulo_beta_02: int = 13
valor_en_radianes_02: float = math.radians(angulo_beta_02)
cateto_adyacente_02: int = 11
hipotenusa_02: float = cateto_adyacente_02 / math.cos(valor_en_radianes_02)
print(hipotenusa_02)
# ejercicio 3
hipotenusa_03: int = 36
cateto_adyacente_03: int = 24
coseno_alfa_03: float = cateto_adyacente_03 / hipotenusa_03
radianes_alfa_03: float = math.acos(coseno_alfa_03)
angulo_alfa_03: float = math.degrees(radianes_alfa_03)
print(angulo_alfa_03)