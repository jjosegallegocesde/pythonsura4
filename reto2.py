mesDigitado=input("Digite el mes que desea evaluar")
mes=mesDigitado.lower()

if(mes=='enero' or mes=='febrero' or mes=='marzo'):
    print(f'estamos en invierno {mes}')
elif(mes=='abril' or mes=='mayo' or mes=='junio'):
    print(f'estamos en primavera {mes}')
elif(mes=='julio' or mes=='agosto' or mes=='septiembre'):
    print(f'estamos en verano {mes}')
elif(mes=='octubre' or mes=='noviembre' or mes=='diciembre'):
    print(f'estamos en otoño {mes}')
else:
    print("mes invalido ")