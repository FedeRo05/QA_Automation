test = "NewEra"
Estado = True
TiempoEj = 0.5
if Estado:
    print(f"El test de {test} Se ha ejecutado en un tiempo de {TiempoEj} segundos")
else: 
    print(f"El test de {test} No se ha ejecutado")

Lista_Usuarios = [
    {"Usuario": "Karen", "Priopridad": "Alta"},
    {"Usuario": "Juan", "Priopridad": "Media"},
    {"Usuario": "Maria", "Priopridad": "Baja"}
]

for i in Lista_Usuarios:
    print(f"El usuario {i['Usuario']} tiene una prioridad {i['Priopridad']}")

puntos = int(input("Ingrese los puntos obtenidos: "))
if puntos >= 80:
    print ("Prueba Aprobada")
else:
    print("Prueba No Aprobada")
