# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define Dayasu = Character("Dayasu")
define c = Character("Ciatripa")
define j = Character("Jaún")
define h = Character("Haón")

#Splashcreen
label splashscreen:
    scene black
    with Pause(1)

    #Advertencia
    show text "Este juego no esta recomendado para personas sensibles a la sangre ni a las mutilaciones. Si sufres patologías como la depresión o similares, aconsejo quitar el juego. No me hago responsable de posibles problemas derivados del consumo de este medio de entretenimiento." with dissolve
    with Pause(8)
    hide text with dissolve
    with Pause(1)

    #Coincidencia
    show text "«Los personajes y hechos retratados en esta obra son completamente ficticios. Cualquier parecido con personas verdaderas, vivas o muertas, o con hechos reales es pura coincidencia»" with dissolve
    with Pause(5)
    hide text with dissolve
    with Pause(1)

    #Créditos
    show text "Una obra de Conejo de la Siniestra" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)

    show text "Gusanos, Lombrices y algo de Muerte" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    
    return

# El juego comienza aquí.

label start:

    stop music fadeout 1

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.
    scene bg prologo
    with fade
    play sound "aire.mp3" loop

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # Presenta las líneas del diálogo.
    "Yacíamos todos aterrados mirando aquella gran fosa. La longitud podría ser perfectamente igual de profunda que la fosa de las marianas." 
    "Lika había caído a lo profundo del gran hoyo. Todos nos quedamos pasmados."
    "Un pequeño desliz y la persona que conocíamos desde hace cuatro años acababa de desaparecer."
    "En lo que podría ser una de las más patéticas muertes."
    "Sin poder hacer algún amago de auxilio, tan solo podíamos quedarnos mirando. Ninguno hablo, tan solo nos quedamos en silencio..."

    scene bg prologo01
    with fade
    stop sound fadeout 0.5
    play sound "sonido_guerra.mp3" fadein 0.5 loop
    "La guerra había devastado la civilización moderna." 
    "El interés económico globalista nos había conducido a esta situación. Cuando empezó la guerra de Ucrania, eso fue el pistoletazo de salida para la que, sin duda, sería la verdadera «Gran Guerra»."
    "Aquella liza entre la nación de Rusia y la nación de Ucrania sería tan solo la base para lo que vendría después."
    "El mundo entro en un ciclo de tensión internacional y de guerras. Desde la tensión serbia-kosovar hasta la guerra iniciada por Hamas en territorio israelí."
    "No se pueden culpar a personas que quieren recuperar un territorio el cual perdieron por culpa de los intereses extranjeros."
    "Pero todo aquello hizo que la industria armamentística funcionara in extremis, produciendo la mayor cantidad de armas."
    "Había más armas que teléfonos móviles en el mundo. En Taiwán, enclave tecnológico para la producción de microchips, fue la principal productora de unidades de procesamiento central destinadas al cálculo bélico."
    "Los estadounidenses utilizaron aquel territorio títere para su propio beneficio, como ya han demostrado en anteriores ocasiones." 
    "Las dos mayores productoras en CPUs, Intel y AMD utilizaron su capital en beneficio de la guerra."
    "Los chinos por aquel tiempo, tenían sus ojos fijos en Taiwán. AMD producía allí sus WAR CHIPS LOGISTICS, ese fue el nombre en clave que acuño la empresa para referirse a sus microprocesadores destinados para el uso militar."
    
    scene bg prologo02
    with dissolve
    "El cuatro de noviembre, China invadió Taiwán en un ataque relámpago. En cuestión de semanas, el gigante asiático había capturado el gran enclave mundial en producción de chips."
    "Por su parte, el gobierno norteamericano no paso por alto esta agresión y le declaro la guerra a China."
    "Siendo está la gota que colmaría el vaso en el conflicto internacional que se nos vendría encima y derivaría en la situación en la que estamos ahora."
    "Sobreviviendo como podemos en cavernas acondicionadas y saliendo al exterior de vez en cuando en busca de recursos y protegiéndonos de la mortífera radiación del exterior."

    scene bg prologo03
    with dissolve
    stop sound fadeout 1.0
    play sound "gente_hablando.mp3" fadein 1.0 loop
    "Tras la declaración de guerra formal con el casus belli de agresión a territorio perteneciente a la OTAN, era el caldo de cultivo más apetitoso para poner en uso y disposición el artefacto atómico." 
    "Más temprano que tarde las agresiones pasarían de campañas militares a los bombardeos nucleares." 
    "Destruyendo así toda la flora, fauna, territorio y bueno, todo a su paso."
    "Dejando una tierra infértil, animales muertos y el agua contaminada."
    "Sin contar todas las vidas humanas que se perdieron en el proceso."

    scene bg gore
    with fade
    stop sound
    play sound "abismo.mp3" fadein 1.0 loop
    "Todavía recuerdo aquel hombre, estaba afectado por la radiación gamma."     
    "Sus pupilas se derretían como se puede derretir el helado en un día caluroso de verano." 
    "Su piel era como la cal escarchada, sobresalía en irregular forma y se caía a pedazos." 
    "Unos pedazos rígidos como el cartón. Y dejaban ver entre las heridas, el más repugnante líquido carmesí saliendo a borbotones." 
    "Todavía me acordare de su cara, una cara que imprimía un ademán de dolor, terror y agonía." 
    "No pude resistir aquello y vomité." 
    "A día de hoy me sigue produciendo pesadillas tan siniestra escena."
    "Y ahora tengo que lidiar con esto, con la muerte de uno de nuestros compañeros." 
    "Empezamos en la caverna siendo dieciocho personas y ahora tan solo somos cinco: Kapo, Jaún, Haón, Ciatripa y yo, Dayasu." 
    Dayasu  "Un pentágono de personas mirando a las grandes fauces que se acababan de tragar a Lika de una única sentada."

    scene bg prologo
    with dissolve
    stop sound fadeout 0.5
    play sound "aire.mp3" loop
    Dayasu "Después de estar un rato mirando el gran agujero, nos miramos entre todos y comprendíamos que deberíamos marcharnos del lugar."
    Dayasu  "Con celeridad nos apartamos de aquella profunda circunvalación y nos reagrupamos unos cuantos metros más lejos."
    Dayasu  "Estuvimos debatiendo por extendido tiempo que deberíamos hacer. La resolución final de aquella acalorada y pasionaria discusión fue el marchar de nuevo hacía la caverna."
    Dayasu "Con las manos vacías volvimos a nuestro refugio. Y con el frío del clima a causa del invierno nuclear y el dolor de perder a una integrante más, tuvimos que volver para estar seguros de las «bestias de la noche»."
    scene bg fauces_animal
    with dissolve
    stop sound
    play sound "bestias_comer.mp3" volume 0.5
    Dayasu "Estos fueron en antaño animales inofensivos."
    Dayasu  "Pero por culpa de la radiación, algunos animales, de los pocos que quedaron, mutaron hasta convertirse en horribles y sanguinarios." 
    Dayasu  "Dejando atrás todo ápice de inofensivos."

    scene bg camino_de_tierra
    with fade
    stop sound
    play sound "sonido_andar.mp3" loop
    Dayasu  "Anduvimos largo tiempo hasta llegar a nuestro refugio."
    Dayasu  "Cuando vimos la pequeña puerta de metal que sobresalía de un conjunto de rocas, respiramos aliviados."
    scene bg puerta_refugio
    with dissolve 
    Dayasu  "Nos apresuramos en llegar lo más rápido posible antes de que cayera la noche tras la finalización del crepúsculo." 
    Dayasu  "Entramos de uno en uno debido al pequeño tamaño del pasadizo que debíamos cruzar." 
    Dayasu  "Siendo yo el último en acceder a la gruta que nos conducía hasta nuestro lugar seguro, me tocaba de responsabilidad cerrar el acceso para evitar que se infiltrara algo indeseado en nuestro hogar."
    scene black
    stop sound fadeout 0.5
    play sound "cerrar_puerta.mp3"  
    Dayasu  "Cerré la puerta teniendo en cuenta de que hiciera el sonido de bloqueo, y que no se quedara en el estado de semi cerrado." 
    Dayasu  "Que por un lado pareciera cerrado pero que en realidad cualquiera la pudiera abrir."
    scene bg pasadizo_refugio
    with dissolve 
    play sound "sonido_pasadizo.mp3" fadein 0.5
    Dayasu  "Después de asegurarme de este hecho, continue con el grupo por el largo y estrecho pasadizo que debíamos cruzar hasta llegar al ascensor. El lugar olía a ciénaga, un olor húmedo y fétido a la vez." 
    Dayasu  "Repugnante para cualquiera y reconfortante para nosotros en esta extrema situación de supervivencia."
    jump capitulo2
    return

    label capitulo2:

        stop sound fadeout 1.0
        play sound "sonido_ascensor.mp3"

        scene black
        with fade

        show text "Quedan 5 supervivientes."
        with Pause (4)
        hide text with dissolve
        with Pause (2)

        "Rato después llegamos al fin al refugio nuclear, aquel lugar, el cual había sido la casa de dieciocho individuos, ahora tan solo era la de cinco." 
        "Cada uno nos dispersamos a nuestras habitaciones." 
        "Yo llegue a la mía cansado y adolorido, no podía quitarme la imagen de Lika cayendo por aquel precipicio."

        scene bg abismo
        with dissolve
        play sound "abismo.mp3" loop

        # Aquí se muestran los sprites y diálogos de los pensamientos de Dayasu. Escena Limbo.
        "Seguramente el ávaro de Jaún le pareció perfecto este hecho."
        show jaun
        with dissolve
        "Ahora, posiblemente, podríamos dividir las pertenencias restantes que quedaban de Lika." 
        "Siempre ha sido Jaún un egoísta, Lika tenía siempre en su mano derecha, en su dedo corazón."
        show jaun_mascara
        with dissolve
        "El más hermoso y litúrgico anillo de plata, regalado por su pretendiente en el día de su boda." 
        "A tan punto llego la obsesión de Jaún por la valerosa pieza de joyería, que, incluso una vez, lo tuvimos que retener entre cuatro, cuando Haón se lo encontró intentando cortarle el dedo a Lika para conseguir su anillo." 
        "También esa es otra, Haón tampoco es trigo limpio."
        hide jaun
        hide jaun_mascara
        with dissolve

        show haon
        with dissolve 
        "Bajo la apariencia de una tierna chica de estatura  bajita, se esconde una farisea puritana." 
        "Siempre va con ese tono arrogante cuando empieza a hablar de los hombres y el sexo."
        show haon_mascara
        with dissolve 
        "Cuando es la primera que estaba desesperada por mantener relaciones sexuales con el primero que se le presentara." 
        "La odio más que a ninguno de los de aquí. Incluso más que a Ciatripa." 
        "Se me hierven la sangre y los jugos gástricos y parece que se me clavan agujas al rojo vivo en mi corazón cuando la veo."
        "Oh… Todavía me acuerdo, me la estuve cruzando durante tres meses. En esos meses solo se dedicó a acosarme y echarme miradas de pícaras." 
        "Ninfa ponzoñosa, bella en su exterior y fea en sus entrañas." 
        "Me estuvo provocando… tonto de mí. Tuve que darme cuenta de sus intenciones, sí, me di cuenta el primer día que la vi." 
        "Pero idiota en ese momento fui, que mi corazón le quise entregar y en ese instante me enamoré de ella profundamente." 
        "Le hable y tuvimos una relación rara, una relación del tira y afloja, una relación de personas que se atraen mutuamente." 
        "Una atracción contradictoria, una parte quería a la otra de manera emocional, y la otra, tan solo quería drenar sus deseos carnales con el primer chico con el que tuviera ocasión." 
        "Algunas veces me pregunto porque no hice caso a mis amigos." 
        "Porque no le hice caso cuando me contó un gran amigo, que cuando lo invito a su casa con unas pocas personas más, apareció en ropa interior." 
        "Mostrando sus bragas y su sujetador. Y que estuvo todo el rato comportándose de manera cariñosa con él." 
        "Ante el poco caso que le hizo mi amistad hacia ella, decidió echarlo de su casa." 
        "Tiempo más tarde me la encontré justo cuando andaba con otra amistad mía. Le saludé y ella fue por su lado y nosotros por el nuestro." 
        "Entonces mí amigo me dijo — ¿Es esa quién yo creo que es? — pregunto en un tono de intriga."
        "Le dije que sí en un tono bajo. No quería que se enterara." 
        "Y unos metros después conversando sobre ella. Salió a relucir el episodio de la ropa interior." 
        "Mi amigo me apelo. — Veo lógico el razonamiento que tuvo. No me follas, pues te hecho de mi casa —. Esa le está tirando a todos a ver si alguno cae y se la folla."
    hide haon
    hide haon_mascara
    with dissolve

    #Narración de los pensamientos sin sprites
    "Aunque en el fondo sabía que sí, decidí ignorar ese comentario." 
    "Si he de decir que en todo momento le di la razón." 
    "Era evidente para lo que me quería. No sabía que tiempo más tarde, por un desliz que tuvo." 
    "Desvelo al completo su desesperación por consumar el acto pasional-lascivo." 
    "Afectándose mi corazón con mal enfermedad sentimental, decidí cortar con ella una vez por todas."
    "No me costó mucho esfuerzo, incluso tuvo otro desliz." 
    "Después de intentar conocerla y decirle de quedar, de buen corazón."
    "Había recibido la mayor y patéticas sartas de mentiras."

    #Se hace una excepción y se muestran los sprites de Jaun y Kapo, para presentar este último.
        
    # Muestra el sprite de Jaun y lo mueve hacía la izquierda.
    show jaun at left
    with dissolve

    # Muestra el sprite de Kapo y lo mueve hacía la derecha.
    show kapo at right
    with dissolve

    "Ya, harto de todo y harto de la gente como Jaún o Kapo." 
    "Que también los conocía de antes y habían escondido su verdadera naturaleza de metamorfosis social en pro de sus intereses."

    #Escondemos ambos sprites
    hide jaun
    with dissolve

    hide kapo
    with dissolve

    # Volvemos a la narrativa sin sprites
    "Le solté con toda la dureza y explicitad que se pueda y de manera elegante la frase de «Era verdad lo que me he enterado, realmente si eres una puta»." 
    "Rápidamente con su ingenio, aunque siempre quisiera taparlo bajo la apariencia de una chica aniñada, fue capaz de ver en la implícita elegancia sintáctica-gramatical el verdadero mensaje." 
    "Gracias a aquello, me facilito el trabajo de capitular con este relato amoroso-sexual."
    "No voy a hacerme el fuerte. Esa noche quería arrancarme el corazón de cuajo."
    "Introducir violentamente la mano en mi lado izquierdo del pecho, penetrar tan profundo y ser capaz de destrozar la carne, grasa, músculos y huesos y llegar hasta el corazón." 
    "Para agarrarlo y tirar de él, al igual que cuando tiras de una tirita para ahorrarte el sufrimiento de arrancarte el bello."

    # Volvemos a exceptuar y mostramos el sprite de Ciatripa para presentar al personaje.

    show ciatripa
    with dissolve
    
    "Ciatripa también me había querido usar para mantener relaciones sexuales." 
    "También se la tengo guardada, y más por intentar usarme como sustituto." 
    "Después de haber roto de una relación e inténtalo con otro, y que tampoco le hiciera caso."
    "Todo aquello ocurrió en el corto lapso de tiempo que me junte con ella. Lo único que le puedo dar, es que fue más sincera, a la hora de dejarme en claro sus verdaderas intenciones."
    
    hide ciatripa
    with dissolve

    # Volvemos a monologar sin sprites.
    "Al contrario que Haón, bajo aquella capa de amor que me intento vender con astucia y que me creí en parte." 
    "Se encontraba una depredadora sexual y una mitómana. Capaz de llorarle a cualquiera a cambio de sexo y luego tener también la cobardía de injuriar con improperios al sexo masculino cuando no se ajustaba al interés de su lívido."

    #Terminamos el capítulo 2
    "Me atormenta la culpa de manera tortuosa sin saber bien el porqué de aquel martirio que sufre mi alma." 
    "No tengo nada que ver en su defunción, fue un accidente." 
    "Esa cara, ese pequeño semblante taciturno antes de caer del todo y terminar con su vida." 
    "No me puedo quitar esa expresión de mi cabeza. Intentaré no darle más vueltas de las necesarias." 
    "Si no, ese recuerdo me flagelará lo suficiente para no poder vivir." 
    "Intentaré dormir esta noche como pueda. Dejaré mi sinapsis en absoluto vació." 
    "Mi res cognitam va estar en blanco puro, igual de claro que el sol, igual de liso que la seda." 
    "Y así mi suerte me aconteció en esta pequeña desventura del sueño."

    scene black
    with fade

    stop sound fadeout 0.5
    play sound "sonido_paso_de_capitulo.mp3"

    show text "Quedan {b}4 supervivientes.{/b}" 
    with dissolve
    with Pause(4)
    
    hide text
    with dissolve
    with Pause(2)

    jump capitulo3

    return
    
    #Capítulo 3
    label capitulo3:
        scene black
        with fade

        "A la mañana siguiente nos encontramos con el cadáver de Kapo."

        scene bg gore
        with dissolve
        play music "puzle_macabro.mp3" loop

        "El shock que sufrimos fue cuanto menos atroz." 
        "El cuerpo que yacía inerte y sin vida en el centro de la habitación."
        "Le habían destrozado la cabeza, seguramente con algún arma blanca del tipo contundente."
        "La fuerza ejercida y las repeticiones del agresor en contra de la cabeza de Kapo, había hecho que se desfigurara." 
        "La carne, la sangre y los sesos manchaban el suelo de la habitación." 
        "Para hacer la escena aún más dantesca, se había entretenido, y a modo de espectáculo jocoso, en insertar un teclado informático en el hueco que dejaba el cuello." 
        "Haciéndole ver como el «hombre ordenador». Esta escenografía propia de un vodevil, era aún más impactante que la muerte de Lika."

        # Discusión entre Jaún y Ciatripa

        "Jaún fue el primero en adelantarse a hablar."

        show jaun
        with dissolve

        j "Me quedo con lo que queda de ordenador."

        "Todos dirigimos nuestros ojos hacía a él en un tono enfurecido y a la vez amargo."

        hide jaun
        with dissolve

        show ciatripa at right
        with dissolve
        c "No tienes sentimientos o que."

        show jaun at left
        with dissolve
        j "¿Sentimientos?"

        "Antes de que todo se fuera de control, di un paso al frente y hablé."

        show haon at center
        with dissolve

        Dayasu  "¡Es que no os dais cuenta o que! ¡Se nos ha colado algo de fuera! Y ha matado a Kapo sin ningún tipo de piedad. Y además es escurridizo."
        Dayasu  "Quién os dice que no puede estar merodeando por la sala. Merodeando por el pasillo. Haciendo vigía por toda la caverna."
        Dayasu  "Incluso puede que este aquí. Esperando para matarnos a todos. A lo mejor no esta observando, viendo, respirando y saboreando nuestro miedo. Relamiéndose como un pervertido. Masturbándose en estos instantes con nuestro pánico."

        "Aquellas palabras calaron en los cuatro restantes. Ninguno se atrevió a llevar la contraria ante aquellas impositivas y nocivas palabras para la espirituosidad del sosiego del ánima."
        "Con el corazón inquieto, con facciones aterradas y con pulso acelerado. Fueron abandonando la sala." 

        hide jaun
        with dissolve
        with Pause(1)
    
        hide ciatripa
        with dissolve
        with Pause(1)
        
        hide haon
        with dissolve
        with Pause(1)

        "Dayasu cerró la puerta."
        play sound "cerrar_puerta.mp3"

        scene black
        with dissolve

        "Haón trajo un papel, celo y un rotulador de color negro."
        show marca_puerta:
            ypos 0.2
            xpos 0.4
        with dissolve
        "Dibujo una X en el papel, que previamente había colocado de manera horizontal y lo colgaron en la puerta como seña de {i}Memento mori.{/i}"


        #Parte final del capítulo 3
        hide marca_puerta
        with dissolve

        stop music fadeout 1.0
        stop sound
        play music "sonido_pasadizo.mp3"

        "Reunidos todos en la sala principal de aquel hormigonado refugio atómico, Jaún seguía de manera pedante y apática reclamando su parte del «pastel» de Lika y Kapo." 
        "Los tres, aunque se llevaban a {i}matar entre sí{/i}, recriminaron su actitud codiciosa sobre los bienes materiales de los presentes difuntos."
        "Tiempo más tarde se dispersaron a su dormitorio." 
        play sound "poner_seguro_puerta.mp3" 
        "El clic del seguro se podía escuchar en las puertas."
        "Tomaron medidas ante esta extraordinaria situación. El tiempo paso, cada segundo parecía una eternidad."
        "Todo el mundo, nervioso por aquellos hechos acontecidos, intentaron dormir, y, uno no despertó."

        stop music fadeout 1.0
        stop sound

        play sound "sonido_paso_de_capitulo.mp3"
        show text "Quedan {b}3 supervivientes.{/b}"
        with dissolve
        with Pause(4)
        
        hide text
        with dissolve
        with Pause(2)

        jump capitulo4

    return

    label capitulo4:
        scene black
        with fade
        play sound "sonido_reloj.mp3"
        "Cinco de la tarde es la hora que marcaba el reloj."
        "El cuerpo de Jaún apareció en la sala principal."

        scene bg gore
        with dissolve
        stop sound fadeout 1.5
        play music "puzle_macabro02.mp3" loop
        "La escena parecía sacada de una película de mafias." 
        "A Jaún le habían cortado el cuello, extraído toda la sangre e insertado en la herida todos los bienes áureos de su posesión." 
        "Los tres que quedábamos vomitamos por la asquerosa situación. ¿Cómo podía ser posible?, es la pregunta que nos hacíamos todos." 
        "Si habíamos acordado cerrar nuestras habitaciones con cerrojos y no salir de ella."
        scene black
        with dissolve

        show marca_puerta:
            ypos 0.2
            xpos 0.4
        with dissolve
        with Pause(2)
        
        hide marca_puerta
        with dissolve
        with Pause(2)

        "De momento me vino la respuesta a la cabeza, salí disparado hacía la habitación de Kapo." 
        "Cuando llegué a aquella precintada estancia en donde yacía el cuerpo destrozado, me percaté que estaba «patas arribas» el lugar." 
        "Los demás llegaron unos instantes más tarde, tras darse cuenta de mi acelerado paso."

        scene habitacion_kapo
        with dissolve

        show ciatripa at left
        with dissolve
        c "¿No me digas qué...?"

        show haon at right
        with dissolve
        h "Insecto."
        with moveinright

        "Efectivamente, Jaún había cometido la imprudencia de ir a {i}robar{/i} los bienes a Kapo." 
        "Nos podíamos hacer una idea de cómo se había desarrollado la situación." 
        "Sin más que añadir al asunto, volvimos a cerrar la habitación de Kapo y nos dirigimos a la de Jaún para señalizarla con una X."

        hide ciatripa
        with dissolve
        with Pause(1)
        
        hide haon
        with dissolve
        with Pause(1)

        play sound "cerrar_puerta.mp3"

        scene black

        "Cuando llegamos a la habitación de Jaún, todos miramos la gran X pintada en rojo de su habitación." 
        show marca_roja:
            ypos 0.2
            xpos 0.4
        with dissolve
        with Pause(1)
        "Esta no estaba situada en su puerta, si no en la pared frontal de su dormitorio." 
        "Horrorizados entramos en pánico."

        hide marca_roja
        with dissolve
        with Pause(1)
        
        scene bg abismo
        with dissolve

        show ciatripa
        with dissolve
        c "¿Cómo es… posible?"

        Dayasu "Algo o alguien nos ha estado vigilando desde lo de Kapo"

        show haon at left
        with dissolve
        h "¿Y sí… realmente el asesino es alguien de nosotros tres?"
        with moveinright

        scene black
        with dissolve
        hide ciatripa
        hide haon
        stop music fadeout 1.0
        play sound "abismo.mp3" loop
        "En ese momento Ciatripa y yo nos volteamos hacía Haón."
        show haon
        with dissolve
        "Ese comentario había hecho que nos helase la sangre."
        "Antes de que pudiera decir nada, Ciatripa se me adelanto y recriminó a Haón."

        hide haon
        with dissolve

        scene bg abismo
        with dissolve
        show haon
        with dissolve
        with Pause(0.5)
        
        c "¡Que estas insinuando!"
        c "¡Es que estas loca o que!"

        hide haon
        with dissolve

        "La reacción de Haón nos dejó aún más en pavor. 
        En vez de enrabietarse como lo hacía siempre;"
        "Bajo la cabeza de una manera inquietante y en su cara se dibujó una sonrisa aterradora."
        scene black
        with dissolve
        show sonrisa_macabra
        with fade
        "Río durante un tiempo."
        play music "risa_elmo.mp3"
        with Pause(3)
        stop music
        
        scene bg abismo
        with dissolve

        show ciatripa
        with dissolve

        c "¡Que te hace tanta gracia!"

        hide ciatripa
        with dissolve

        show haon
        with dissolve

        h "¿Y si uno de nosotros es el villano?"

        hide haon
        with dissolve

        show ciatripa
        with dissolve

        c "¡Eres una puta!"

        hide ciatripa
        with dissolve

        "Justamente en el instante en el que se mencionó la palabra puta, Haón dejo de reír." 
        "Levanto despacio su cabeza y fijo una mirada tórrida hacia Ciatripa."

        show ciatripa at left
        with dissolve
        with Pause(1)

        show haon
        with dissolve
        with Pause(1)

        h "¡Me has llamado puta!"
        h "¡Quién te crees que eres!" 
        h "¡Tú eres la más puta de aquí, te has follado a todo al que has querido, tan solo por tu beneplácito y placer!"
        
        "Ciatripa no se achanto ante estas ofensas de Haón."

        c "¡Puta yo, mírate zorra asquerosa! ¡Siempre vas vestida como una fulana!"
        c "¡Te crees que no me he dado cuenta como mirabas a todo el mundo!"
        c "¡Siempre le fijabas una mirada lasciva!"
        c "¡Y cuando apareció el tonto de turno, fuiste directa a follartelo!"
        c "¡Te tendrías que mirar en un espejo, puta mal nacida!"


        "Cuando termino aquella reyerta de malas palabras. Ambas se quedaron sin una pizca de energía." 
        "Entonces propuse salir únicamente en los ratos de comer."
        "Para tener la seguridad de los cerrojos de nuestros cuartos, y que, en tal caso de que el peligro lo tuviéramos en el interior, {i}no nos gastara ninguna otra broma de mal gusto.{/i}"

        #Comienza la recta final hacia el fin de la historia.
        scene black
        with fade
        stop sound fadeout 0.5
        hide haon
        hide ciatripa

        show text "Tiempo más tarde"
        with dissolve
        with Pause(4)

        hide text
        with dissolve
        with Pause(2)
        
        scene bg sala_principal
        with dissolve

        play music "sonido_pasadizo.mp3" fadein 1.0 loop

        "Se hallaban Ciatripa y Haón en la sala principal comiendo la comida enlatada para evitar cualquier tipo de envenenamiento."

        show ciatripa
        with dissolve
        c "¿Qué raro?"

        show haon at right
        with dissolve
        h "¿Qué es raro?"

        c "Dijimos de esperar a Dayasu un rato antes de ponernos a comer. En todo el rato que llevábamos no ha aparecido."
        h "¿Quieres decir…?"

        "Un silencio cubrió toda aquella gran sala."
        "Ciatripa volteo con violencia su cabeza y dirigió su mirada hacia el reloj analógico."

        play sound "sonido_reloj.mp3"
        scene black
        with dissolve
        hide ciatripa
        hide haon

        "Marcaban las diez y cuarto de la noche."

        "Ciatripa volvió su cabeza hacia su interlocutora Haón."
        show haon
        with dissolve
        with Pause(1)
        
        "La mirada de Ciatripa hacia Haón fue el suficiente signo de comunicar alerta."
        hide haon
        with dissolve
        with Pause (0.5)

        stop sound fadeout 0.5
        play sound "sonido_caja.mp3"

        "Ambas chicas se levantaron de aquellas cajas y corrieron hacía la habitación de Dayasu, temiéndose la peor de las calamidades."

        scene black
        with dissolve
        stop music fadeout 1.0
        "Plantadas en frente de aquella puerta, Haón giro del pomo." 
        "Una desagradable sensación recorrió el cuerpo de las dos jóvenes." 
        "La puerta estaba sin ningún seguro y se podía abrir."

    return