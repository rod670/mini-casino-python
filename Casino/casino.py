print("************************************")
print("            Bienvenido              ")
print("************************************")
import random
saldo = 1000
while True:
    print("1._ Jugar dados")
    print("2._ Jugar a adivinar el número")
    print("3:_ Ver saldo")
    print("4._ Retirar saldo")
    print("5._ Salir del casino")
    opcion = input("Elija una opción paea jugar: ")
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion == 5: break
        if opcion == 4:
            if saldo > 0:
                while True:
                    retiro = input("Ingresa el monto que deseas retirar: ")
                    if retiro.isdigit():
                        retiro = int(retiro)
                        if retiro <= saldo:
                            saldo -= retiro
                            billete100 = retiro // 100
                            retiro = retiro % 100
                            billete50 = retiro // 50
                            retiro = retiro % 50
                            billete20 = retiro // 20
                            retiro = retiro % 20
                            billete10 = retiro // 10
                            retiro = retiro % 10
                            billete5 = retiro // 5
                            retiro = retiro % 5
                            billete1 = retiro
                            print("Se te hace la entrega de tu saldo de la siguiente manera: ")
                            print(f"Billetes de 100: {billete100}")
                            print(f"Billetes de 50: {billete50}")
                            print(f"Billtes de 20: {billete20}")
                            print(f"Billetes de 10: {billete10}")
                            print(f"Billetes de 5: {billete5}")
                            print(f"Billetes de 1: {billete1}")
                            break
                        else:
                            print("Saldo insuficiente. Vuelva a ingresar un mnonto mayor o igual a su saldo actual.")
                    else:
                        print("Ingresa únicamente numeros mayores a 0")
                break
        elif opcion == 1:
            print("******************************")
            print("         Instrucciones        ")
            print("******************************")
            print("- El juego consiste en lanzar los dados")
            print("- Si la suma de los dados es igual a 7 o a 11, ganaste. De lo contrario, perdiste.")
            while True:
                print(f"Tu saldo actual es de {saldo} dólares")
                monto = input("Ingrese el monto que desea apostar: ")
                if monto.isdigit():
                    monto = int(monto)
                    if monto <= saldo:
                        saldo = saldo - monto
                        dado1 = random.randint(1,6)
                        dado2 = random.randint(1,6)
                        print(f"Dado 1: {dado1}")
                        print(f"Dado 2: {dado2}")
                        if dado2 + dado1 == 7 or dado1 + dado2 == 11:
                            print("Felicidades, ganaste.")
                            ganancia = monto * 2
                            saldo += ganancia
                            print(f"Se te suma a tu cuenta {ganancia} dolares")
                        else:
                            print("Perdiste :(")
                        break
                    else:
                        print("Saldo insuficiente. Vuelve a ingresar un monto a apostar. Asegurate de ingresar un monto menor o igual a tu saldo actual")
                else:
                    print("Monto inválido. Ingresa únicamenre un número mayor a 0")
        elif opcion == 2:
            print("******************************")
            print("         Instrucciones        ")
            print("******************************")
            print("- En este juego vas a tener que adivinar el número que yo estoy pensando")
            print("- Tendrás 1 solo intento para adivinar")
            print("- El número a adivinar está entre el 1 y el 10")
            while True:
                monto = input("Ingresa el monto que deseas apostar: ")
                if monto.isdigit():
                    monto = int(monto)
                    if monto <= saldo:
                        saldo -= monto
                        numero = random.randint(1,10)
                        adivina = input("Ingresa el número que crees que es el correcto: ")
                        if adivina.isdigit():
                            adivina = int(adivina)
                            if adivina == numero:
                                print("Felicidades, ganaste.")
                                ganancia = monto * 2
                                print(f"Ganaste {ganancia} dolares")
                                saldo += ganancia
                            else:
                                print("Número incorrecto :(")
                                print(f"El número correcto es: {numero}")
                            break
                        else:
                            print("Perdiste :(")
                            break
                    else:
                        print("Saldo insufieciente. Ingresa únicamente un monto menor o igual a tu saldo actual")
                else:
                    print("Monto inválido. Ingresa únicamente un número mayor a 0")
        elif opcion == 3:
            print(f"Tu saldo actual es de: {saldo}")
        else:
            print("Opción inválida. Ingresa únicamente las opciones disponibles")