"""Integrantes del eqipo:
    - ...
    - Pimentel Gonzalez Ricardo Antonio
    - Taboada Montiel Enrique
    
    Practica 1: Akinator
    
"""
print("Piensa en algo, y yo tratare de adivinarlo con pregiuntas de si o no")

respuesta = input("Estas pensando en algo real?  (si/no): ").strip().lower()

if respuesta == "si":
    respuesta = input("¿Es un ser vivo? (si/no): ").strip().lower()
    
    if respuesta == "si":
        respuesta = input("¿Es un animal? (si/no): ").strip().lower()
            
        if respuesta == "si":
            respuesta = input("¿Es un mamifero? (si/no): ").strip().lower()
            
            if respuesta == "si":
                respuesta = input("¿Es carnivoro? (si/no): ").strip().lower()
                
                if respuesta == "si":
                    respuesta = input("¿Es un felino? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta == input("¿Es domestico? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("pensaste e un gato.")
                        else:
                            print("Pensaste en un leon/tigre")
                    else:
                        respuesta = input("¿Es un oso? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un oso")
                        else:
                            print("Pensanste en un lobo/zorro")
                            
                else:
                    respuesta = input("¿Es un animal grande? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("¿Tiene trompa? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un elefante")
                        else:
                            respuesta = input("Tiene cuernos? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un venado/alce")
                            else:
                                print("Pensaste en un caballo o una vaca")
                    else:
                        print("Pesaste en un conejo/roedor")
                        
            else:
                respuesta = input("Es un ave? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("Vuela? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en un aguila o un halcon. ")
                    else:
                        print("Pensaste en un pinguino o avestruz")
                else:
                    respuesta = input("Es un respitl o anfibio? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta == input("Es venenoso? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en una serpiente/rana venenosa.")
                        else:
                            print("Pensaste en una tortuga/lagarto")
                    else:
                        print("Pensaste en un pez/criatura marina")
        else:
            respuesta = input("¿Es una planta? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Da frutos? (si/no): ").strip().lower()
                if respuesta == "si":
                    print("Pensaste en un árbol frutal o una vid.")
                else:
                    print("Pensaste en una planta ornamental o medicinal.")
            else:
                respuesta = input("¿Es una persona? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es un personaje histórico? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en un rey, presidente o científico.")
                    else:
                        respuesta = input("¿Es un personaje famoso? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un actor, cantante o deportista.")
                        else:
                            respuesta = input("¿Es un profesionista? (si/no): ").strip().lower()
                            if respuesta == "si":
                                respuesta = input("¿Es de area fisico-matematicas? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un ingeniero, matematico, arquitecto o fisico.")
                                else:
                                    respuesta = input("¿Es de area de la salud? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en un doctor, enfermera o paramedico, psicologo.")
                                    else:
                                        respuesta = input("¿Es de area de humanidades? (si/no): ").strip().lower()
                                        if respuesta == "si":
                                            print("Pensaste en un filosofo, escritor o historiador.")
                                        else:
                                            respuesta = input("¿Es de area de social-administrativa? (si/no): ").strip().lower()
                                            if respuesta == "si":
                                                print("Pensaste en un abogado, administrador o contador.")
                                            else:
                                                respuesta = input("¿Es de area de artes? (si/no): ").strip().lower()
                                                if respuesta == "si":
                                                    print("Pensaste en un pintor, escultor o músico.")
                                                else:
                                                    respuesta = input("¿Es de area de educacion? (si/no): ").strip().lower()
                                                    if respuesta == "si":
                                                        print("Pensaste en un profesor, pedagogo.")
                            else:
                                respuesta = input("¿Se dedica a un oficio? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un carpintero, plomero o electricista.")
                                else:
                                    print("Pensaste en un campesino, pescador o minero.")                                                
                else:
                    respuesta = input("¿Es un hongo? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en un hongo comestible o venenoso.")
    else:
        respuesta = input("¿Es un objeto? (si/no): ").strip().lower()

        if respuesta == "si":
            respuesta = input("¿Se encuentra en una casa? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Se usa en la cocina? (si/no): ").strip().lower()
                if respuesta == "si":
                    print("Pensaste en un sartén, cuchillo o licuadora.")
                else:
                    respuesta = input("¿Es un electrodoméstico? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en una lavadora, refrigerador o televisor.")
                    else:
                         respuesta = input("¿Produce luz? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("¿Funciona con electricidad? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en una bombilla.")
                        else:
                            print("Pensaste en una vela.")
                    else:
                        respuesta = input("¿Es un mueble? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en una silla, mesa o sofá.")
                        else:
                            respuesta = input("¿Se usa para la limpieza? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en una escoba, trapeador o detergente.")
                            else:
                                respuesta = input("¿Se usa para la higiene personal? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en una toalla, cepillo de dientes o jabón.")
                                else:
                                    print("Pensaste en otro objeto del hogar.")

            else:
                respuesta = input("¿Es una herramienta? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Se usa en la construcción? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en un martillo, serrucho o taladro.")
                    else:
                        print("Pensaste en una llave inglesa o una pinza.")

                else:
                    respuesta = input("¿Es un medio de transporte? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("¿Es terrestre? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un coche, motocicleta o bicicleta.")
                        else:
                            print("Pensaste en un barco o avión.")
                    else:
                        print("Pensaste en un dispositivo tecnológico como una computadora o consola.")

        else:
            respuesta = input("¿Es algo del espacio? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Es un planeta? (si/no): ").strip().lower()
                if respuesta == "si":
                    print("Pensaste en Marte, Júpiter o la Tierra.")
                else:
                    print("Pensaste en una estrella, cometa o galaxia.")
            else:
                print("Pensaste en algo desconocido o abstracto.")

else:
    respuesta = input("¿Es un concepto imaginario? (si/no): ").strip().lower()
    if respuesta == "si":
        respuesta = input("¿Es un personaje de ficción? (si/no): ").strip().lower()
        if respuesta == "si":
            respuesta = input("¿Es un superhéroe? (si/no): ").strip().lower()
            if respuesta == "si":
                print("Pensaste en Batman, Superman o Spider-Man.")
            else:
                respuesta = input("¿Es una criatura mitologica? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es de la mitologia griega? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en un minotauro, centauro o hidra.")
                    else:
                        respuesta = input("¿Es de la mitologia nórdica? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un troll, elfo o valquiria.")
                        else:
                            respuesta = input("¿Es de la mitologia egipcia? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un dios o faraón.")
                            else:
                                respuesta = input("¿Es de la mitologia china? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un dragon o fénix.")
                                else:
                                    print("Pensaste en un ser mitológico de otra cultura.")
                else:
                    respuesta = input("¿Es un personaje de cuento o libro? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en Cenicienta, Peter Pan o Sherlock Holmes.")
                    else:
                        respuesta = input("¿Es un personaje de videojuego? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en Mario, Sonic o Lara Croft.")
                        else:
                            print("Pensaste en un personaje de película o serie.")
    else:
        respuesta = input("¿Es un mundo ficticio? (si/no): ").strip().lower()
        if respuesta == "si":
            print("Pensaste en un universo de ciencia ficción o fantasia.")
        else:
            print("Pensaste en un concepto filosófico o abstracto.")

print("¡Juego terminado!")