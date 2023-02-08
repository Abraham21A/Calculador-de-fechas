# Codigo para calcular la diferencia en años entre un año actual y otro año introducido por el usuario

while True:

  # Solicitar y validar el año actual introducido por el usuario
  while True:
    current_date = input("introduzca el año actual: ")
    if len(current_date) == 4: # Verificar que sea un valor de 4 digitos 
      try:
        current_date = int(current_date) # Convertir a entero
        break # Salir del ciclo si es un año valido
      except ValueError:
        print("valor incorrecto, ingrese una fecha valida")
    else:
      print("ingrese un valor de 4 digitos")

  # Solicitar y validar el otro año para calcular
  while True:
    date_to_calculate = input("introduzca otro año para calcular: ")
    if len(date_to_calculate) == 4: # Verificar que sea un valor de 4 digitos
      try:
        date_to_calculate = int(date_to_calculate) # Convertir a entero
        break # Salir del ciclo si es un año valido
      except ValueError:
        print("valor incorrecto, ingrese una fecha valida")
    else:
      print("ingrese un valor de 4 digitos")

  # Calcular la diferencia de años y presentar un mensaje
  if date_to_calculate == current_date:   # Verifica si los años son iguales
    print("Ha introducido el mismo año que el actual")
  elif date_to_calculate < current_date: # Verifica si el año es anterior al año actual
    years_passed =  current_date - date_to_calculate
    if years_passed == 1:  # Verifica si han pasado 1 año o más
      print("Han pasado {} año desde el año {} que has introducido".format(years_passed, date_to_calculate))
    else:
      print("Han pasado {} años desde el año {} que has introducido".format(years_passed, date_to_calculate))
  # Verifica si el año es posterior al año actual
  else:
    years_reach =  date_to_calculate - current_date
    if years_reach == 1: # Verifica si falta 1 año o más
      print("falta {} año para llegar {} al año que has introducido".format(years_reach, date_to_calculate))
    else:
      print("falta {} años para llegar {} al año que has introducido".format(years_reach, date_to_calculate))

  # Preguntar al usuario si desea volver a utilizar el programa
  play_again = input("¿Desea volver a utilizar el programa? (si/no): ")
  if play_again.lower() != "si":
    break

