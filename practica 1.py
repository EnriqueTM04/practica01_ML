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
            respuesta = input("¿Es un vertebrado? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Es un mamifero? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es un animal domestico? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en un perro, gato o conejo.")
                    else:
                        respuesta = input("Pone huevos? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un ornitorrinco o equidna.")
                        else:
                            respuesta = input("¿Es un marsupial? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un canguro, koala o zarigüeya.")
                            else:
                                respuesta = input("¿Es un animal omnivoro? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un oso, cerdo.")
                                    respuesta = input("¿Es un animal carnivoro? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en un león, tigre o lobo.")
                                    else:
                                        respuesta = input("¿Es un animal herbívoro? (si/no): ").strip().lower()
                                        if respuesta == "si":
                                            respuesta = input("¿Es un animal rumiante? (si/no): ").strip().lower()                                        
                else:
                    respuesta = input("¿Es un ave? (si/no): ").strip().lower()
                    if respuesta =="si":
                        respuesta = input("¿Es un ave domestica? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un canario, gallina o pato.")
                        else:
                            respuesta = input("¿Puede volar? (si/no): ").strip().lower()
                            if respuesta == "si":
                                respuesta = input("¿Es nocturno? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un búho o lechuza.")
                                else:
                                    print("Pensaste en un águila, halcón o colibrí.")
                            else:
                                respuesta = input("¿Es un ave acuatica? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un pato, cisne o flamenco.")
                                else:
                                    print("Pensaste en un ave terrestre.")
                                    respuesta = input("¿Es de lo hemisferios polo norte o sur? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en un pinguino o albatros.")
                                    else:
                                        print("Pensaste en un avestruz o emú.")
                    else:
                        respuesta = input("¿Es un reptil? (si/no): ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("¿Es un reptil terrestre? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en una serpiente, lagartija o cocodrilo.")
                            else:
                                print("Pensaste en una tortuga o iguana.")
                        else:
                            respuesta = input("¿Es un anfibio? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en una rana o salamandra.")
                            else:
                                respuesta = input("¿Es un pez? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    respuesta = input("¿Es un pez de agua dulce? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en una trucha, carpa o bagre.")
                                    else:
                                        print("Pensaste en un pez de agua salada.")                    
                    
            else:
                respuesta = input("¿Es un invertebrado? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es un insecto? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en una mariposa, abeja o escarabajo.")
                    else:
                        respuesta = input("¿Es un aracnido? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en una araña o escorpión.")
                        else:
                            respuesta = input("¿Es un molusco? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un caracol o pulpo.")
                            else:
                                respuesta = input("¿Es un crustaceo? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un cangrejo o langosta.")
                                else:
                                    respuesta = input("¿Es un Miriápodos (ciempiés y milpiés)? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en un ciempiés o milpiés.")
                                    else:
                                        respuesta = input("¿Tiene simetria radial, como una estrella ? (si/no): ").strip().lower()
                                        if respuesta == "si":
                                            print("Pensaste en una estrella de mar o erizo de mar.")
                                        else:
                                            respuesta = input("¿Es un gusano? (si/no): ").strip().lower()
                                            if respuesta == "si":
                                                print("Pensaste en una lombriz o gusano de seda.")
                                        
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
                    respuesta = input("¿Es una estrella? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en el Sol o Sirio.")
                    else:
                        respuesta = input("¿Es un satélite? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en la Luna o un satélite artificial.")
                        else:
                            respuesta = input("¿Es un asteroide? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un asteroide o cometa.")
                            else:
                                respuesta = input("¿Es un fenómeno astronómico? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un eclipse o lluvia de estrellas.")

            else:
                respuesta = input("¿Es un concepto? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es una emocion? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en amor, odio o tristeza.")
                    else:
                        respuesta = input("¿Es un valor? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en justicia, libertad o respeto.")
                        else:
                            respuesta = input("¿Es un fenómeno natural? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un arcoíris, tormenta o terremoto.")
                            else:
                                respuesta = input("¿Es un concepto matemático? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un número, operación o figura geométrica.")
                                else:
                                    respuesta = input("¿Es un concepto científico? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en una teoría, ley o experimento.")
                                    else:
                                        print("Pensaste en un concepto filosófico o abstracto.")
                    
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
                        respuesta = input("¿Es un dios o semidios? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en Zeus, Hades o Aquiles.")
                        else:
                            print("Pensaste en un centauro, minotauro o gorgona.")
                    else:
                        respuesta = input("¿Es de la mitologia nórdica? (si/no): ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("¿Es un dios o gigante? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en Thor, Odín o Loki.")
                            else:
                                print("Pensaste en un elfo, enano o troll.")
                        else:
                            respuesta = input("¿Es de la mitologia egipcia? (si/no): ").strip().lower()
                            if respuesta == "si":
                                respuesta = input("¿Es un dios o faraón? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en Ra, Anubis o Cleopatra.")
                                else:
                                    print("Pensaste en un escarabajo, serpiente o esfinge.")
                            else:
                                respuesta = input("¿Es de la mitologia china? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    respuesta = input("¿Es un dios o dragón? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en Buda, Shenlong o Hotei.")
                                    else:
                                        print("Pensaste en un qilin, fénix o jiangshi.")
                                else:
                                    print("Pensaste en un ser mitológico de otra cultura.")
                                    
                else:
                    print("Pensaste en un fantasma, aparicion.")
    else:
        respuesta = input("¿Es un mundo ficticio? (si/no): ").strip().lower()
        if respuesta == "si":
            print("Pensaste en un universo de ciencia ficción o fantasia.")
        else:
            print("Pensaste en un concepto filosófico o abstracto.")

print("¡Juego terminado!")