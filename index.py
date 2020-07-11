#paquete que permite el manejo de hojas de cálculo de Excel. 
# Es necesario instalar paquete Pandas en el equipo
import pandas as p

#Leer los archivos de libros y personas.
# No vi forma de trabajar con una ruta relativa a la ubicación de index.py, 
# así que es necesario actualizar la ruta.
libros = p.read_excel(r'C:\Users\adria\Desktop\data\r_libros.xlsx')
personas = p.read_excel(r'C:\Users\adria\Desktop\data\r_personas.xlsx')
prestamos = []
#Guardar ambas listas como diccionarios.
#Alternativa a verlo directamente en el Data Frame extraído 
#de las hojas de cálculo
l_libros = libros.to_dict()
l_personas = personas.to_dict()

#Función que permite ver la lista principal de personas
def verPersonas():
    opcion = input("Por favor elija el formato deseado para ver el registro de personas.\na - Tabla de Datos \nb - Lista ordinaria\n")
    if opcion == 'a':
        #imprimir Data frame de personas extraído del archivo
        print(personas)
    
    elif opcion == 'b':
        #recorrer diccionario e imprimir datos de las personas
        for indice in range (0, len(l_personas['Identificación'])):
            print("CEDULA: " + str(l_personas["Identificación"][indice]) + "\nNOMBRE: " + l_personas["Nombre"][indice] + "\nPRIMER APELLIDO: " + l_personas["Primer Apellido"][indice] + "\nSEGUNDO APELLIDO: " + l_personas["Segundo Apellido"][indice] + "\nE-MAIL: " + l_personas["Correo Electrónico"][indice] + "\n------------------------------------")
    else:
        print(str(opcion) + " no es una opcion valida. Por favor intente de nuevo.")
        verPersonas()
    input("\nPresione la tecla enter para regresar al menu principal")
    menu()

#Función que ordena la lista de personas por número de cédula
def ordenarPersonas():
    #El ordenamiento puede ser por cualquiera de las columnas
    #imprimir desde Data frame ordenado por primer apellido
    dataOrdenada = personas.sort_values('Primer Apellido')
    print(dataOrdenada)
    input("\nPresione la tecla enter para regresar al menu principal.\n")
    menu()

#Función que muestra el registro de la persona en el índice brindado por el usuario
def registroPersona(indice):
    opcion = input("Por favor elija el formato deseado para ver el registro de esta persona.\na - Tabla de Datos \nb - Lista ordinaria\n")
    if opcion == 'a':
        #imprimir fila indicada por el usuario desde Data frame de personas extraído del archivo
        print(personas.loc[[indice]])
    elif opcion == 'b':
        #imprime fila indicada por el usuaro desde diccionario
        print("CEDULA: " + str(l_personas["Identificación"][indice]) + "\nNOMBRE: " + l_personas["Nombre"][indice] + "\nPRIMER APELLIDO: " + l_personas["Primer Apellido"][indice] + "\nSEGUNDO APELLIDO: " + l_personas["Segundo Apellido"][indice] + "\nE-MAIL: " + l_personas["Correo Electrónico"][indice])    
    else:
        print(str(opcion) + " no es una opcion valida. Por favor intente de nuevo.")
    input("\nPresione la tecla enter para regresar al menu principal")
    menu()

#Función que permite ver la lista principal de libros
def verLibros():
    opcion = input("Por favor elija el formato deseado para ver el registro de libros.\na - Tabla de Datos \nb - Lista ordinaria\n")
    if opcion == 'a':
        #imprimir Data frame de libros extraído del archivo
        print(libros)
    elif opcion == 'b':
        #recorrer diccionario e imprimir datos de los libros
        for indice in range (0, len(l_libros['ID'])):
            print("ID: " + str(l_libros["ID"][indice]) + "\nNOMBRE: " + str(l_libros["Nombre"][indice]) + "\nGENERO: " + l_libros["Género"][indice] + "\nAUTOR: " + l_libros["Autor"][indice] + "\n------------------------------")
    else:
        print(str(opcion) + " no es una opcion valida. Por favor intente de nuevo.")
        verLibros()
    input("\nPresione la tecla enter para regresar al menu principal")
    menu()

#Función para buscar libro por coincidencia parcial o total con cadena de caracteres comparado con el nombre del libro
def buscarLibro():
    criterio = str(input("Por favor ingrese el valor que dese utilizar como criterio de búsqueda: \n"))
    for indice in range (0, len(l_libros["ID"])):
            if criterio in str(l_libros["Nombre"][indice]):
                print(libros.loc[[indice]])
    input("\nPresione la tecla enter para regresar al menu principal ")
    menu()

#Función para registrar el préstamo de un libro
def prestarLibro():
    print(personas)
    entrada = input("\nIngrese la posición en la lista de la persona a quien desea entregar el libro:\n")
    try:
        p_persona = int(entrada)
    except ValueError:
        print("El valor a ingresar debe ser un numero entero, por favor intente de nuevo.\n")
        prestarLibro()
    if p_persona < 0 or p_persona > len(l_personas['Identificación']) - 1:
        print("El valor a ingresar no puede ser mayor que la cantidad de personas en la lista, por favor intente de nuevo.\n")
        prestarLibro()
    else:
        print(libros)
        entradaL = input("\nIngrese el ID del libro que desea prestar a " + personas["Nombre"][p_persona] + ":\n")
        try:
            idLibro = int(entradaL)
        except ValueError:
            print("El valor a ingresar debe ser un numero entero, por favor intente de nuevo.\n")
            prestarLibro()
        print("\nLibro seleccionado:\n")
        print(libros.loc[[idLibro - 1]])
        idPersona = l_personas["Identificación"][p_persona]
        nombrePersona = l_personas["Nombre"][p_persona]
        #variable para enviar a lista de prestamos
        id_Libro = l_libros["ID"][idLibro - 1]
        prestamo = {"idPersona" : idPersona, "idLibro" : id_Libro}
        prestamos.append(prestamo)
        print("\n Prestamo registrado con exito.\n")
        menu()

#Función para mostrar lista de préstamos de libros
def verPrestamos():
    print(prestamos)
    for i in range(0, len(prestamos)):
        for j in range(0, len(l_libros['ID'])):
            if l_libros['ID'][j] == prestamos[i]['idLibro']:
                nombreLibro = l_libros['Nombre'][j]
                break
        for k in range(0, len(l_personas['Identificación'])):
            if l_personas['Identificación'][k] == prestamos[i]['idPersona']:
                nombrePersona = l_personas["Nombre"][k]
        print("\nID del prestamo: " + str(i) + "\n" + "ID de usuario: " + str(prestamos[i]['idPersona']) + "\n" + "Nombre de usuario: " + nombrePersona + "\n" + "ID del libro: " + str(prestamos[i]['idLibro']) + "\n" + "Nombre del libro: " + nombreLibro + "\n ------------------------------")
    input("Presione la tecla enter para regresar al menu principal: ")
    menu()
#menú principal del programa
def menu():
    print("\nGracias por utilizar nuestro sistema de control.")
    print("A continuacion, por favor introduzca la letra correspondiente a la accion que desea realizar.\n")
    opcion = input("a - Ver lista de personas \nb - Ordenar lista de personas \nc - Imprimir registro especifico de persona \nd - Ver lista de libros \ne - Buscar libro \nf - Prestar libro \ng - Ver prestamos de libros \nh - Salir\n")
    if opcion == 'a':
        verPersonas()
    elif opcion == 'b':
        ordenarPersonas()
    elif opcion == 'c':
        indice = input("Indique el numero de registro que desea ver: \n")
        #Validación para evitar error al ingresar número entero fuera de rango o valor diferente a un número entero
        try:
            i = int(indice)
        except ValueError:
            print("El valor a ingresar debe ser un numero entero, por favor intente de nuevo.\n")
            menu()
        if int(indice) > personas.last_valid_index():
                print("***Por favor indique un numero valido con base en la lista existente de personas. \n")
                verPersonas()
        else:
            registroPersona(int(indice))
    elif opcion == 'd':
        verLibros()
    elif opcion == 'e':
        buscarLibro()
    elif opcion == 'f': 
        prestarLibro()
        menu()
    elif opcion == 'g':
        verPrestamos()
        menu()
    elif opcion == 'h':
        exit()
    else:
        print("\nPor favor introduzca la letra correspondiente a una de las opciones presentes en el menu.")
        menu()
menu()