#Javiera Funezalida y Catalina Villegas

import csv

def imprimir():
    print("Seleccionó imprimir lista de notebooks prestados")
    if verificar_notebooks():
        with open(nombre_archivo,'w') as archivo:
            escritor=csv.writer(archivo)
            for estudiante in notebooks_prestados:
                escritor.writerow(estudiante)
            print("Se imprimio la lista exitosamente")
    else:
        print("No hay notebooks prestados")
        
def verificar_notebooks():
    valido=True
    if notebooks_prestados==[]:
        print("No se han prestado notebooks")
        valido=False
    return valido

def verificar_rut(rut):
    valido=False
    for estudiante in notebooks_prestados:
        if estudiante[0]==rut:
            valido=True
    return valido

def registrar_datos():
    estudiante=[]
    print("Debe registrarse para solicitar un notebook\nFavor de dar sus datos :D")
    print('')
    try:
            rut=(input("ingrese su rut, sin digito verificador: "))
            if len(rut) == 8:
                estudiante.append(rut)
                print('')
                nombre=input("Ingrese su nombre: ")
                estudiante.append(nombre)
                print('')
                apellido=input("Ingrese su apellido: ")
                estudiante.append(apellido)
                print('')
                documento_entregado=input("Documento a entregar (Carnet o pase escolar): ")
                if documento_entregado.upper() == "CARNET" or documento_entregado.upper()=="PASE ESCOLAR":
                    estudiante.append(documento_entregado)
                    print('')
                    while True:
                        print(f"Numero de notebooks disponibles: {notebooks}")
                        numero_notebook=int(input("Ingrese el número de notebook a pedir: "))
                        if numero_notebook>31 or numero_notebook<=0 or numero_notebook not in notebooks:
                            print("Ese número de notebook no existe")
                        else:
                            print("Notebook registrado correctamente")
                            estudiante.append(numero_notebook)
                            notebooks.remove(numero_notebook)
                            notebooks_prestados.append(estudiante)
                            break
                else:
                    print("Documento no válido, intente con carnet o pase escolar")
            else:
                print("Datos no válidos :C")
    except NameError:
        print("variable no esiste xaval")
    except TypeError:
        print("Pongale voluntad y escriba bieeeen")
    except Exception as e:
        print(f"diabloooo{e}")

def devolver():
    try:
        if verificar_notebooks():
            rut=input("Ingrese el rut: ")
            print('')
            if verificar_rut(rut):
                for estudiante in notebooks_prestados:
                    if estudiante[0]==rut:
                        notebooks.append(estudiante[4])
                        notebooks.sort()
                        notebooks_prestados.remove(estudiante)
                        print("Se entrego exitosamente el notebook")
            else:
                print("El rut ingresado no está registrado con un notebook")
    except ValueError:
        print("Ingrese solo números solicitados")

def modificar():
    try:
        try:
            if verificar_notebooks():
                rut=input("Ingrese el rut: ")
                if verificar_rut(rut):
                    print(f"Numero de notebooks disponibles: {notebooks}")
                    try:
                        numero_notebook=int(input("Ingrese el numero del nuevo notebook prestado: "))
                        if numero_notebook in notebooks:
                            for estudiante in notebooks_prestados:
                                if estudiante[0]==rut:
                                    notebooks.append(estudiante[4])
                                    notebooks.remove(numero_notebook)
                                    notebooks.sort()
                                    estudiante[4]=numero_notebook
                                    print("Se cambio el notebook exitosamente")
                        else:
                            print("El notebook esta prestado en este momento")
                    except ValueError:
                        print("Ingrese número de notebook válido")
                else:
                    print("El rut ingresado no esta registrado con notebook")

        except ValueError:
            print("Asegurese de tener 8 digitos de longitud y solo números")
            print('')  
    except Exception as e:
        print(f"ta mal {e}")

def menu():
    print("----------------------")
    print(f"Notebooks prestados: {len(notebooks_prestados)}")
    print("")
    print("1. Prestar notebooks")
    print("2. Devolver notebooks")
    print("3. Modificar préstamo de notebooks")
    print("4. Imprimir la lista de notebooks prestados")
    print("5. Terminar clase")


try:
    print("Bienvenido")
    nombre_profe=input("Ingrese el nombre del docente: ")
    print('')
    curso=input("Ingrese la sigla del ramo actual: ")
    print('')
    seccion=input("Ingrese la sección actual: ")
    print('')
    if nombre_profe!='' and curso!='' and seccion!='':
        nombre_archivo=nombre_profe+' '+curso+'-'+seccion+'.csv'

        notebooks=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        notebooks_prestados=[]
        while True:
            menu()
            try:
                opcion=int(input("Ingrese su opción: "))
            except ValueError:
                print("Ingrese un número D:")
            print("----------------------")

            if opcion==1:
                print("Selecciono prestar notebooks")
                registrar_datos()

            elif opcion==2:
                print("Seleccionó devolver notebooks")
                devolver()
            
            elif opcion==3:
                print("Seleccionó modificar un prestamo de notebook")
                modificar()

            elif opcion==4:
                try:
                    imprimir()
                except FileNotFoundError:
                    print("Archivo no encontrao")
                except NameError:
                    print("waos")

            elif opcion==5:
                print("Seleccionó terminar la clase")
                print("Espere a confirmar que todos los notebooks han sido devueltos")
                if verificar_notebooks()==False:
                    print("Todos los notebooks han sido devueltos")
                    print("Bai Bai")
                    break
                else:
                    print("Aun faltan notebooks")
            else:
                print("Ingrese opción válida")
    else:
        print("Ingrese datos, no se admiten espacios -.-")           
except Exception as a:
    print(f"diavlo{a}")