# -*- coding: utf-8 -*-

import pilasengine
pilas = pilasengine.iniciar()


class MrDNA_menu(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen = "adn2.png"


class MrDNA_juego(pilasengine.actores.Actor):
	def iniciar(self):
		self.imagen = "adn.png"



class EscenaMenu(pilasengine.escenas.Escena):
	def iniciar(self):
		self.fondo_menu = pilas.fondos.Galaxia()
		
		dialogo=pilas.actores.Dialogo()
		self.adn_menu = MrDNA_menu(pilas)
		self.adn_menu.escala=0.8
		self.adn_menu.x=180
	
		dialogo.decir(self.adn_menu, "Presiona en mi")
		dialogo.decir(self.adn_menu, "Si respondes 5 veces bien ganas, si erras 2 veces pierdes")
								  

		dialogo.comenzar()
		
		self.Mi_Menu = pilas.actores.Menu(
			[
				(u"Jugar", self.Ir_al_juego),
				# (u"Ayuda", self.Ayuda),
				(u"Salir", self.Salir_de_Pilas)
			])
		
		Nombre_de_juego = pilas.actores.Texto(u"Mr DNA")
		Nombre_de_juego.color = pilas.colores.rojo
		Nombre_de_juego.y = 170

	def actualizar(self):
		pass
		
	# def Ayuda(self):
	# 	pilas.escenas.EscenaAyuda()
		
	def Salir_de_Pilas(self): 
		pilas.terminar()	
		
	def Ir_al_juego(self): 
		pilas.escenas.EscenaJuego()		

# class EscenaAyuda(pilasengine.escenas.Escena):
# 	def iniciar(self):
# 		self.fondo_juego=pilas.fondos.Noche()
# 		self.fondo_juego.imagen="fondodeljuego1.png"
# 		self.Boton_Volver =pilas.interfaz.Boton("Volver al Menu")
# 		self.Boton_Volver.y = 220
# 		self.Boton_Volver.x = 250
# 		self.Boton_Volver.conectar(self.Volver)
		
# 	def Volver(self):	
# 		pilas.escenas.EscenaMenu()
		
# 	def actualizar(self):
# 		pass	


class Adn(pilasengine.actores.Banana):
	def iniciar(self):
		self.imagen = "adn-icon.png"
		self.imagen.escala=0.1


class EscenaJuego(pilasengine.escenas.Escena):		
	def iniciar(self):
		self.nombre=raw_input("Ingrese su nombre: ")
		self.lista=[[u"¿Cuál es la técnica de laboratorio que \n perfeccionó Rosalind Franklin?",u"La cristalografía de rayos X",u"La espectroscopía de resonancia magnética nuclear",u"La microscopía electrónica"],
					[u"¿Cómo está compuesto un nucleótido?",u"Base nitrogenada+Azúcar+Grupo Fosfato",u"Ester+Cadena Carbonada ",u"Grupo Fosfato+Base hidrogenada"],
					[u"¿En qué sentido lee el ADN polimerasa las cadenas de ácidos nucleicos?",u"5 prima a 3 prima",u"De derecha a izquierda",u"3 prima a 5 prima"], 
					[u"¿A qué tipo de estructura pertenecen las representaciones alpha helice y beta plegada?", "Estructura Secundaria","Estructura Primaria ","Estructura Cuartenaria"],                                                                                                                                                                                                    
					[u"¿Cuales son los 4 tipos de nucleótidos del ADN?", "Adenina,Timina,Citocina y Guanina","Adenosina,Tirosina,Guanina y Citosina", "Acitocina,Tasina,Guatisina y Carisina"],
					[u"¿Cómo se denomina la región promotora para la codificación de diversos genes?",u"Caja TATA (TATAAA)",u"Caja GAGA (GAGAA)",u"Caja ATAC (AATACC)"],
					[u"¿Qué es un gen?",u"Un segmento de ADN con una secuencia particular de nucleotidos",u"Un segmento de ARN",u"Toda la informacion contenida en el ADN de una celula"],
					[u"En las células eucariotas, ¿en qué estructura celular se almacena la información genética?",u"Núcleo", "Mitocondrias", "Aparato de Golgi"],
					[u"¿Cuántos ácidos nucleicos forman un codón?", "3", "2", "4"],
					[u"¿Cómo se denomina al ARN que contiene al codón ?", "ARN Mensajero","ARN Transferencia","ARN Ribosomal"]]
	
		self.fondo_juego = pilas.fondos.Galaxia()
		 
		self.puntaje = pilas.actores.Puntaje(color="rojo") #self
		self.puntaje.x = -150 #self
		self.puntaje.y = -190 #self
		self.puntaje.valor = 0 #añadido
		self.correctosaparecer=pilas.actores.Texto("Correctos:")
		self.correctosaparecer.x=-220
		self.correctosaparecer.y=-190
		
		self.error=pilas.actores.Puntaje(color="rojo")
		self.error.valor=0
		self.error.x=-150
		self.error.y=-220
		self.incorrectosaparecer=pilas.actores.Texto("Incorrectos:")
		self.incorrectosaparecer.x=-230
		self.incorrectosaparecer.y=-220
		
		self.adn_juego = MrDNA_juego(pilas)
		#self.imagen = "adn.png"
		self.adn_juego.escala = 0.7 #añadido, el adn_juego era muy grande
		self.adn_juego.aprender('arrastrable') #modificado
		self.adn_juego.aprender('MoverseConElTeclado') #modificado
		self.adn_juego.decir("Bienvenido/a "+ self.nombre + " puedes arrastrarme")
		self.adn_juego.x=[0,200],1
		
		self.Boton_Volver =pilas.interfaz.Boton("Volver al Menu")
		self.Boton_Volver.y = -220
		self.Boton_Volver.x = 250
		self.Boton_Volver.conectar(self.Volver)
		
		
		#Agrego las colisiones
		pilas.colisiones.agregar('adn', 'mrDNA_juego', self.sintetiza)#añadido
		
		#Agrego tarea
		pilas.tareas.agregar(3, self.Preguntando)
		
	def Reiniciar(self):
    # Obtiene todos los actores de la pantalla.
		actores = pilas.actores.listar_actores()

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.puntaje, self.fondo_juego, self.adn_juego,self.error,self.correctosaparecer,self.incorrectosaparecer,self.Boton_Volver]:
				actor.eliminar()

    # Genera una pregunta nueva
		self.Preguntando()
		
	def Preguntando(self):	
		self.b1 = Adn(pilas)
		self.b1.x = -280
		self.b1.y = 100
		self.b1.esverdadera = False
		self.b2 = Adn(pilas)
		self.b2.x = -280
		self.b2.y = 0
		self.b2.esverdadera = False
		self.b3 = Adn(pilas)
		self.b3.x = -280
		self.b3.y = -100
		self.b3.esverdadera = False
		
		self.poslista=pilas.azar(0,len(self.lista)-1)
		self.encuentrapreg=self.lista[self.poslista][0]
		self.mostrar_pregunta=pilas.actores.Texto(self.encuentrapreg)
		self.mostrar_pregunta.y=180
		self.mostrar_pregunta.ancho=500
		self.mostrar_pregunta.escala=1
		
		self.respuesta_correcta = self.lista[self.poslista][1] #Respuesta Correcta
		self.respuesta_incorrecta_1 = self.lista[self.poslista][2] #Respuesta incorrecta 1
		self.respuesta_incorrecta_2 = self.lista[self.poslista][3] #Respuesta incorrecta 2

		self.lista.pop(self.poslista) #Se saca de la lista de preguntas asi no se repiten preguntas en una partida

		self.rta_1 = pilas.actores.Texto("")
		self.rta_1.x=-120
		self.rta_1.y=100
		self.rta_1.ancho=300
		self.rta_1.escala=0.7
		self.rta_2 = pilas.actores.Texto("")
		self.rta_2.x=-120
		self.rta_2.y=0
		self.rta_2.ancho=300
		self.rta_2.escala=0.7
		self.rta_3 = pilas.actores.Texto("")
		self.rta_3.x=-120
		self.rta_3.y=-100
		self.rta_3.ancho=300
		self.rta_3.escala=0.7
		
		#Adn verdadero
		self.adns_posibles = [self.b1,self.b2,self.b3]
		self.textos_posibles = [self.rta_1,self.rta_2,self.rta_3]
		self.indiceok=pilas.azar(0,2)
		self.adn_verdadera=self.adns_posibles[self.indiceok]
		self.adn_verdadera.esverdadera=True
		self.texto_respuesta_verdadera=self.textos_posibles[self.indiceok]
		self.texto_respuesta_verdadera.texto=self.respuesta_correcta
		
		if self.b1.esverdadera:
			self.rta_1.texto=self.respuesta_correcta
			self.rta_2.texto = self.respuesta_incorrecta_1
			self.rta_3.texto = self.respuesta_incorrecta_2
		elif self.b2.esverdadera:
			self.rta_2.texto=self.respuesta_correcta
			self.rta_1.texto = self.respuesta_incorrecta_1
			self.rta_3.texto = self.respuesta_incorrecta_2
		elif self.b3.esverdadera:
			self.rta_3.texto= self.respuesta_correcta
			self.rta_1.texto = self.respuesta_incorrecta_1
			self.rta_2.texto = self.respuesta_incorrecta_2
				
	def ganaste(self):
		actores = pilas.actores.listar_actores()

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.adn_juego]:
				actor.eliminar()
		self.fondo_juego=pilas.fondos.Espacio()
		self.Boton_Volver =pilas.interfaz.Boton("Volver al Menu")
		self.Boton_Volver.y = 220
		self.Boton_Volver.x = 250
		self.Boton_Volver.conectar(self.Volver)
		self.puntajefinal=pilas.actores.Texto(str(self.puntaje.valor))
		self.puntajefinal.escala=2
		self.cartelfelicidades=pilas.actores.Texto("Felicidades "+self.nombre+" has ganado")
		self.cartelfelicidades.y=220
		self.cartelfelicidades=pilas.actores.Texto("Mr DNA esta feliz!")
		self.cartelfelicidades.y=150
		self.cartelpuntaje=pilas.actores.Texto("Tu puntaje es: ")
		self.cartelpuntaje.x=-100
		self.errorestotales=pilas.actores.Texto(str(self.error.valor))
		self.errorestotales.y=-100
		self.errorestotales.escala=2
		self.cartelerror=pilas.actores.Texto("Cantidad de errores: ")
		self.cartelerror.x=-150
		self.cartelerror.y=-100
		self.adn_juego.imagen = "cup.png"
		self.adn_juego.x=180


	def perdiste(self):
		actores = pilas.actores.listar_actores()

    # Elimina todos los actores excepto el fondo y el puntaje
		for actor in actores:
			if actor not in [self.adn_juego]:
				actor.eliminar()
		self.fondo_juego=pilas.fondos.Espacio()
		self.Boton_Volver =pilas.interfaz.Boton("Volver al Menu")
		self.Boton_Volver.y = 220
		self.Boton_Volver.x = 250
		self.Boton_Volver.conectar(self.Volver)
		self.puntajefinal=pilas.actores.Texto(str(self.puntaje.valor))
		self.puntajefinal.escala=2
		self.cartelfelicidades=pilas.actores.Texto(self.nombre+ " PERDISTE :(")
		self.cartelfelicidades.y=220
		self.cartelfelicidades=pilas.actores.Texto("Mr DNA se enfermo")
		self.cartelfelicidades.y=150
		self.cartelpuntaje=pilas.actores.Texto("Tu puntaje es: ")
		self.cartelpuntaje.x=-100
		self.errorestotales=pilas.actores.Texto(str(self.error.valor))
		self.errorestotales.y=-100
		self.errorestotales.escala=2
		self.cartelerror=pilas.actores.Texto("Cantidad de errores: ")
		self.cartelerror.x=-150
		self.cartelerror.y=-100
		self.adn_juego.imagen = "adn_perdi.png"


	def Volver(self):	
		pilas.escenas.EscenaMenu()
		
	def actualizar(self):
		pass	
		
	def sintetizaSIEMPRE_CORRECTO(self, adns, adn_juego):
		#ESO ES SOLO PARA PRUEBAS SIEMPRE CORRECTO
		if self.puntaje.valor < len(self.lista):
			adns.eliminar() #hay que eliminar adn colisionado
			adn_juego.rotacion=[0,360]
			adn_juego.decir("Muy bien")
			estrella = pilas.actores.Estrella()
			estrella.x = adns.x
			estrella.y = adns.y
			estrella.escala = 0.2
			estrella.escala = [2, 1] * 2
			self.puntaje.aumentar()
			pilas.tareas.agregar(3, self.Reiniciar)
		else:
			pilas.avisar("Felicidades has ganado")
			self.puntaje.aumentar()
			self.ganaste()

	def sintetiza(self, adns, adn_juego):
		if not adns.esverdadera: 
			if self.error.valor<1:
				pilas.camara.vibrar()
				adns.eliminar()
				#adn_juego.gritar()
				#dialogo=pilas.actores.Dialogo()
				adn_juego.decir("MAL MAL MAL")
				self.error.aumentar() #aumenta 1 error. En total puede ser hasta 3 errores.
				pilas.tareas.agregar(3, self.Reiniciar)
				
			else:
				pilas.avisar("Fin del juego")
				self.error.aumentar()
				self.perdiste()
				
		else:
			if self.puntaje.valor<4:
				adns.eliminar() #hay que eliminar adn colisionado
				adn_juego.rotacion=[0,360]
				adn_juego.decir("Muy bien")
				estrella = pilas.actores.Estrella()
				estrella.x = adns.x
				estrella.y = adns.y
				estrella.escala = 0.2
				estrella.escala = [2, 1] * 2
				self.puntaje.aumentar()
				pilas.tareas.agregar(3, self.Reiniciar)
			else:
				pilas.avisar("Felicidades has ganado")
				self.puntaje.aumentar()
				self.ganaste()
				
		
	def Volver(self):	
		pilas.escenas.EscenaMenu()
		
	def actualizar(self):
		pass
		

#pilas.escenas.vincular(EscenaAyuda)
pilas.escenas.vincular(EscenaMenu)
pilas.escenas.vincular(EscenaJuego)

pilas.escenas.EscenaMenu()

pilas.ejecutar()