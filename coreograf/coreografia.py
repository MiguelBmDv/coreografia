import time
estado = input("¿Estás listo para la coreografía? Responde si o no: ")


while estado.lower() == "si":
    for mov in range(1,5):
        print("Realicemos el movimiento {}:\n".format(mov))
        time.sleep(2)
        if mov == 1:
           
            print("Bien empecemos..... \n  -Pon tus brazos al frente y estiralos.")
            time.sleep(5)
            print("  -Empuña tus manos y que cada palma este mirando a la otra.")
            time.sleep(5)
            print("  -Mueve tus manos de arriba abajo pero en ritmo distinto, es decir una inicia arriba y otra abajo.")
            time.sleep(5)
            print("  -Abre tus piernas, y ponte en posicion de sentadilla pero elevada.")
            time.sleep(5)
            print("  -Mueve la cadera como si dieras saltos pequeños pero sin elevar la planta del pie, y repite todos los pasos para generar un movimiento constante.\n")
            time.sleep(5)
            print("  -Haz 10 Repeciticiones de brazos.")

        elif mov == 2:
            
            print("  -Lo primero es abrir las piernas.")
            time.sleep(5)
            print("  -Como demostración moveras la pierna izquierda detras de la derecha de forma diagonal, conservando la pierna derecha en el mismo lugar.")
            time.sleep(5)
            print("  -Ahora detente y vuelve al centro... sube el brazo izquierdo a la altura de la cabeza. \n  -Combinaras este paso con el anterior en uno solo, es decir cada vez que vayas hacia atras en una direccion subiras el brazo del mismo lado de la pierna hacia la altura de la cabeza, y cuando vuelvas al centro, lo bajaras.")
            time.sleep(15)
            print("  -Ahora realiza el paso izquierdo combinado, luego repite con el lado derecho el paso combinado.")
            time.sleep(5)
            print("  -Haz los dos pasos combinados por 5 repeticiones.\n")
            time.sleep(5)
            
        elif mov == 3:
            
            print("  -Realizaremos el movimiento de manos del baile macarena.")
            time.sleep(5)
            print("  -Primero estira los brazos hacia al frente, pon las palmas hacia afuera.")
            time.sleep(5)
            print("  -Luego pon las palmas hacia arriba.")
            time.sleep(5)
            print("  -Ahora pon en puño tus manos aun con los brazos estirados, luego abre la mano y vuelve a poner las palmas hacia afuera.")
            time.sleep(5)
            print("  -Repite los pasos anteriores 5 veces.\n")
            time.sleep(5)

        elif mov == 4:
            
            print("  -Realizaremos otro movimiento de manos con cadera.")
            time.sleep(5)
            print("  -Primero estira los brazos hacia arriba, y los moveras de un lado a otro.")
            time.sleep(5)
            print("  -Mientras tanto, mueve el tronco del cuerpo al ritmo de los brazos y la cancion.")
            time.sleep(5)
            print("  -Repite los pasos anteriores 3 veces.\n")
            time.sleep(5)


    print("Adiós, la coreografía ha terminado.")
    time.sleep(5)
    estado = input("¿Quieres seguir repitiendo la coreografía? Responde si o no: ")
if estado.lower() == "no":
    print("Esta bien, que tenga buen dia :)")
else:
    print("Opcion no valida")
