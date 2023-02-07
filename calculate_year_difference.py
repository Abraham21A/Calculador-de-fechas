while True:
  
  while True:
    current_date = input("introduzca el año actual: ")
    if len(current_date) == 4:
      try:
        current_date = int(current_date)
        break
      except ValueError:
        print("valor incorrecto, ingrese una fecha valida")
    else:
      print("ingrese un valor de 4 digitos")

  while True:
    date_to_calculate = input("introduzca otro año para calcular: ")
    if len(date_to_calculate) == 4:
      try:
        date_to_calculate = int(date_to_calculate)
        break
      except ValueError:
        print("valor incorrecto, ingrese una fecha valida")
    else:
      print("ingrese un valor de 4 digitos")
  
  if date_to_calculate == current_date:
    print("Ha introducido el mismo año que el actual")
  elif date_to_calculate < current_date:
    years_passed =  current_date - date_to_calculate
    if years_passed == 1:
      print("Han pasado {} año desde el año {} que has introducido".format(years_passed, date_to_calculate))
    else:
      print("Han pasado {} años desde el año {} que has introducido".format(years_passed, date_to_calculate))
  else:
    years_reach =  date_to_calculate - current_date
    if years_reach == 1:
      print("falta {} año para llegar {} al año que has introducido".format(years_reach, date_to_calculate))
    else:
      print("falta {} años para llegar {} al año que has introducido".format(years_reach, date_to_calculate))

  play_again = input("¿Desea volver a utilizar el programa? (si/no): ")
  if play_again.lower() != "si":
    break

