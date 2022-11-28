password = input("Ingrese la contraseña:\n")

if len(password) >= 8:
    print('Señor usuario')

    if password == 'Cbhas123':
        print("La contraseña ingresada es correcta")
    else:
        print("Su contraseña es incorrecta")
else:
    print('Señor usuario,\nsu contraseña es incorrecta,')

    if password != 'Cbhas123':
        print("ya que debe tener al menos 8 dígitos.")
