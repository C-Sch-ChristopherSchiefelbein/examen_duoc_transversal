import random
import csv
import math

trabajadores = [
  "Juan Pérez", 
  "María García", 
  "Carlos López", 
  "Ana Martínez", 
  "Pedro Rodríguez", 
  "Laura Hernández", 
  "Miguel Sánchez", 
  "Isabel Gómez", 
  "Francisco Díaz", 
  "Elena Fernández"
]

def sueldo_random():
  sueldos = []
  for i in range(10):
    sueldo = random.randint(300000, 2500000)
    sueldos.append(sueldo)
  return sueldos

def clasificar_sueldos(sueldos):
  bajos = []
  medios = []
  altos = []

  for i in range(len(sueldos)):
    if sueldos[i] < 800000:
      bajos.append((trabajadores[i], sueldos[i]))
    elif sueldos[i] >= 800000 and sueldos[i] <= 2000000:
      medios.append((trabajadores[i], sueldos[i]))
    else:
      altos.append((trabajadores[i], sueldos[i]))

  print("Sueldos menores a $800.000")
  for trabajador, sueldo in bajos:
    print(trabajador + ": $" + str(sueldo))
  print("\nSueldos entre $800.000 y $2.000.000")
  for trabajador, sueldo in medios:
    print(trabajador + ": $" + str(sueldo))
  print("\nSueldos superiores a $2.000.000")
  for trabajador, sueldo in altos:
    print(trabajador + ": $" + str(sueldo))

def ver_estadisticas(sueldos):
  max_sueldo = max(sueldos)
  min_sueldo = min(sueldos)
  suma_sueldos = 0
  log_sueldos = 0

  for sueldo in sueldos:
    suma_sueldos += sueldo
    log_sueldos += math.log(sueldo)

  promedio_sueldo = suma_sueldos / len(sueldos)
  media_geometrica = math.exp(log_sueldos / len(sueldos))

  print("Sueldo más alto: $" + str(max_sueldo))
  print("Sueldo más bajo: $" + str(min_sueldo))
  print("Promedio de sueldos: $" + str(promedio_sueldo))
  print("Media geométrica: $" + str(media_geometrica))

def reporte_sueldos(sueldos):
  reporte = []

  for i in range(len(sueldos)):
    sueldo = sueldos[i]
    descuento_salud = sueldo * 0.07
    descuento_afp = sueldo * 0.12
    sueldo_liquido = sueldo - descuento_salud - descuento_afp
    reporte.append([trabajadores[i], sueldo, descuento_salud, descuento_afp, sueldo_liquido])

  #CSV
  with open('reporte_sueldos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
    for linea in reporte:
      writer.writerow(linea)

  for linea in reporte:
    print("\n",linea[0] + ": Sueldo Base: $" + str(linea[1]) + ",\n Descuento Salud: $" + str(linea[2]) + 
       ",\n Descuento AFP: $" + str(linea[3]) + ",\n Sueldo Líquido: $" + str(linea[4]))

def menu():
  sueldos = []
  while True:
    print("\nMenú de opciones:")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opcion = int(input("\nSeleccione una opción: "))

     
    if opcion == 1:
      sueldos = sueldo_random()
      print("\nSueldos asignados aleatoriamente.")

    elif opcion == 2:
      if len(sueldos) > 0:
        clasificar_sueldos(sueldos)
      else:
        print("\nPrimero debe asignar los sueldos.")

    elif opcion == 3:
      if len(sueldos) > 0:
        ver_estadisticas(sueldos)
      else:
        print("\nPrimero debe asignar los sueldos.")

    elif opcion == 4:
      if len(sueldos) > 0:
        reporte_sueldos(sueldos)
      else:
        print("\nPrimero debe asignar los sueldos.")

    elif opcion == 5:
      print("""\n
            Finalizando programa...
            Desarrollado por Christopher Schiefelbein
            RUT 20.673.415-9
            """)
      break
    else:
      print("\nOpción no válida. Intente nuevamente.")
menu()

