#creditos a la calculadora del cholohatwhite que me ayudo como referencia, lo demas lo hice todo YOOOOOOOOOOOOO AAA gobinet te amo <3 na deaaa re puto
import os

def banner():
  print("\033[37m")
  print("""
   
CALCULADORA DE FISICA 
(si me equivoco en alguna formula perdon xd)
    
    by: vulk4n0           *
    1)densidad            *
    2)velocidad           *
    3)velocidad inicial   * 
    4)velocidad final     *
    5)aceleracion         *
    6)fuerza              *
    7)presion             * 
   -------------------------
   """)
   
  print("")

def densidad():
    print()
    m = float(input("Introduce la masa(en kilogramos): "))
    print()
    v = float(input("introduce el volumen(en litros): "))
    r = m/v
    print()
    print(f"La densidad del cuerpo es de: {r:.2f}")
    n1 = int(input("\n ¿Quieres hacer otra operacion?\n 1)si\n 2)no\n Respuesta: "))
    if n1 == 1:
      os.system("clear")
      os.system("python3 calcufisic.py")
    else:
      print("Gracias por utilizarme :D")

def velocidad():
    print()
    d = float(input("Introduce la distancia en metros: "))
    print()
    t = float(input("introduce el tiempo en segundos: "))
    r = d/t
    print()
    print(f"La velocidad del cuerpo es de:{r:.2f} m/s")
    n1 = int(input("\n ¿Quieres hacer otra operacion?\n 1)si\n 2)no\n Respuesta: "))
    if n1 == 1:
      os.system("clear")
      os.system("python3 calcufisic.py")
    else:
      print("Gracias por utilizarme :D")

def velocidad_inicial():
    print()
    vf = float(input("Introduce la velocidad final: "))
    print()
    a = float(input("introduce la aceleracion: "))
    print()
    t = float(input("introduce el tiempo en segundos: "))
    r = vf - ( a * t )
    print()
    print(f"La velocidad inicial del cuerpo es de:{r:.2f}")
    n1 = int(input("\n ¿Quieres hacer otra operacion?\n 1)si\n 2)no\n Respuesta: "))
    if n1 == 1:
      os.system("clear")
      os.system("python3 calcufisic.py")
    else:
      print("Gracias por utilizarme :D")

def velocidad_final():
    print()
    v0 = float(input("Introduce la velocidad inicial: "))
    print()
    a = float(input("introduce la aceleracion: "))
    print()
    t = float(input("introduce el tiempo en segundos: "))
    r = v0 + a * t
    print()
    print(f"La velocidad final del cuerpo es de:{r:.2f}")
    n1 = int(input("\n ¿Quieres hacer otra operacion?\n 1)si\n 2)no\n Respuesta: "))
    if n1 == 1:
      os.system("clear")
      os.system("python3 calcufisic.py")
    else:
      print("Gracias por utilizarme :D")

def aceleracion():
    print()
    vi = float(input("Introduce la velocidad inicial: "))
    print()
    vf = float(input("introduce la velocidad final: "))
    print()
    t = float(input("introduce el tiempo en segundos: "))
    r = (vf/vi)/t
    print()
    print(f"La aceleracion del cuerpo es de:{r:.2f} m/s^2")
    n1 = int(input("\n ¿Quieres hacer otra operacion?\n 1)si\n 2)no\n Respuesta: "))
    if n1 == 1:
      os.system("clear")
      os.system("python3 calcufisic.py")
    else:
      print("Gracias por utilizarme :D")

def fuerza():
    print()
    a = float(input("Introduce la aceleracion: "))
    print()
    m = float(input("introduce la masa: "))
    print()
    r = m * a
    print()
    print(f"La fuerza es:{r:.2f} Newton")
    n1 = int(input("\n ¿Quieres hacer otra operacion?\n 1)si\n 2)no\n Respuesta: "))
    if n1 == 1:
      os.system("clear")
      os.system("python3 calcufisic.py")
    else:
      print("Gracias por utilizarme :D")

def presion():
    print()
    M = float(input("Introduce la masa: "))
    print()
    A = float(input("introduce el area(en metros): "))
    print()
    r = (M*9.8) / A
    print()
    print(f"La presion es :{r:.2f} Pa ")
    n1 = int(input("\n ¿Quieres hacer otra operacion?\n 1)si\n 2)no\n Respuesta: "))
    if n1 == 1:
      os.system("clear")
      os.system("python3 calcufisic.py")
    else:
      print("Gracias por utilizarme :D")

banner()

op = int(input("Escribe Un Numero Del 1 al 7 : "))

if op == 1:
	densidad()
	
if op == 2:
	velocidad()

if op == 3:
	velocidad_inicial()

if op == 4:
	velocidad_final()
	
if op == 5:
	aceleracion()
	
if op == 6:
	fuerza()
	
if op == 7:
	presion()
	


	
"""
densidad
velocidad
aceleracion
fuerza
presion
"""
