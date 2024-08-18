# Diccionario para almacenar los usuarios y contrasenas
BD = {}


def registro():
    """ 
    Registra un nuevo usuario en el diccionario BD
    Solicita el nombre de usuario y la contrasena, y los agrega al diccionaro
    """
    # Solicitamos nombre de usuario y contrasena al usuario
    nombre_usuario = input('Ingresa tu nuevo nombre de usuario: ').strip()
    contrasena_usuario = input('Ingrese tu nueva contrasena: ').strip()
    
    # Validamos que ambos campos no esten vacios
    if not nombre_usuario or not contrasena_usuario:
        print('El nombre de usuario y la contrasena no pueden estar vacios')
        return

    # Verifica si el usuario ya está registrado
    if nombre_usuario in BD:
        print('El usuario ya está registrado.')
    else:
        # Agrega el nuevo usuario al diccionario
        BD[nombre_usuario] = contrasena_usuario
        print('Usuario creado exitosamente')


def leerData(BD):
    """ 
    Muestra la informacion almacenada en el diccionario BD
    """
    print(f'La informacion almacenada es \n {BD}')


def guardarArchivo(BD, archivo):
    """ 
    Guarda la informacion de los usuarios y contrasenas en un archivo .txt
    Parametros:
    BD (dict): Diccionario que contiene los usuarios y contrasenas
    archivo (str): Nombre del archivo en el que se guardara la informacion
    """
    try:
        with open(archivo, 'w') as file:
            # Escribir cada usuario y contrasena en una linea del archivo
            for usuario, contrasena in BD.items():
                file.write(f'{usuario},{contrasena}\n')
        print(f'Informacion guardada en {archivo}.')
    except IOError as e:
        # Manejo de errores en casode problemas al abrir o escribir en el archivo
        print(f'Error al guardar la informacion en {archivo}: {e}')


def login(BD):
    """ 
    Permite al usuario iniciar sesion verficando el nombre de usuario y la contrasena

    Parametros:
    BD (dict): Diccionario que contiene los usuarios y contrasenas
    """
    intentos = 0
    max_intentos = 3
    while intentos < max_intentos:
        # Solicita nombre de usuario y contrasena para iniciar sesion
        nombre_usuario = input('Ingrese el nombre de usuario: ').strip()
        contrasena_usuario = input('Ingrese la contrasena: ').strip()

        # Verifica si el nombre de usuario esta registrado
        if nombre_usuario in BD:
            # Verifica si la contrasena es correcta
            if BD[nombre_usuario] == contrasena_usuario:
                print('Inicio de sesion exitosa')
                return # Salimos de la funcion al inicio se sesion exitoso
            else:
                print('Contrasena incorrecta')
        else:
            print('Nombre no registrado')
        
        # Incremetamos el contardor de intentos
        intentos += 1
        # Mostramos numeros de intentos restantes
        print(f'Tiene {max_intentos - intentos} intento(s) restante(s)')
    
    # Mensaje finalk si se agotan los intentos
    print('Has superado el numero maximo de intentos. Itenta de nuevo mas tarde')


# Nombre del archivo para guardar la informacion de los usuarios
archivo = 'usuarios.txt'

registro()
registro()
leerData(BD)
guardarArchivo(BD, archivo)
login(BD)
