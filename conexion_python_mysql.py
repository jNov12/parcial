import mysql.connector
from datetime import datetime

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="basedatos1",
    port='3306'
)



def AgregarTarea(Descripcion):
    # Crea un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()
    # Sentencia SQL para insertar una tarea en la tabla
    instruccion = "INSERT INTO Tarea (Descripcion, FechaCreacion, Completada) VALUES (%s, %s, %s);"
    
    #Fecha de la computadora
    FechaCreacion = datetime.now()

    # Valores para la instrucción SQL
    valores = (Descripcion, FechaCreacion, False)
    
    # Ejecuta la sentencia SQL con los valores proporcionados
    cursor.execute(instruccion, valores)
    
    # Guarda los cambios en la base de datos
    conexion.commit()
    cursor.close()

def VerTareas():
    # Crea un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()
    
    # Sentencia SQL para seleccionar tareas de la tabla Tarea
    instruccion = "SELECT ID, Descripcion, FechaCreacion, Completada FROM Tarea"
    
    # Ejecuta la sentencia SQL
    cursor.execute(instruccion)
    
    # Recupera todos los registros de la tabla Tarea
    tareas = cursor.fetchall()
    
    # Imprime las tareas en la consola
    print("=== Lista de Tareas ===")
    for tarea in tareas:
        tarea_id, descripcion, fecha_creacion, completada = tarea
        print(f"ID: {tarea_id}, Descripcion: {descripcion}, Fecha de Creacion: {fecha_creacion}, Completada: {'Si' if completada else 'No'}")
    
    # Cierra el cursor
    cursor.close()

def EliminarTarea(ID):
    # Crea un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()
    
    # Verificar si la tarea con el ID proporcionado existe
    cursor.execute(f"SELECT * FROM Tarea WHERE ID = {ID}")
    tarea_existente = cursor.fetchone()
    
    # Si la tarea no existe, imprimir un mensaje y salir de la función
    if tarea_existente is None:
        print(f"Tarea con ID {ID} no encontrada.")
        cursor.close()
        return
    
    # Si la tarea existe, proceder con la eliminación
    instruccion = f"DELETE FROM Tarea WHERE ID = {ID}"
    cursor.execute(instruccion)
    
    # Guarda los cambios en la base de datos
    conexion.commit()
    print(f"Tarea con ID {ID} eliminada exitosamente.")
    
    # Cierra el cursor
    cursor.close()

def MarcarTareaComoCompletada(ID):
    # Crea un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    # Verificar si la tarea con el ID proporcionado existe
    cursor.execute(f"SELECT * FROM Tarea WHERE ID = {ID}")
    tarea_existente = cursor.fetchone()

    # Si la tarea no existe, imprimir un mensaje y salir de la función
    if tarea_existente is None:
        print(f"Tarea con ID {ID} no encontrada.")
        cursor.close()
        return

    # Si la tarea existe, marcarla como completada
    instruccion = f"UPDATE Tarea SET Completada = True WHERE ID = {ID}"
    cursor.execute(instruccion)

    # Guarda los cambios en la base de datos
    conexion.commit()
    print(f"Tarea con ID {ID} marcada como completada.")

    # Cierra el cursor
    cursor.close()



opcion=0
while opcion != 5:
    print("===Menu de Inicio===")
    print("1. Agregar Tarea")
    print("2. Marcar Tarea como Completada")
    print("3. Ver Tareas")
    print("4. Eliminar Tarea")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("===Agregar Tarea===")
        Descripcion = input("Ingrese la descripcion de la tarea: ")
        AgregarTarea(Descripcion)
        print("Tarea Agregada")
    elif opcion==2:
        VerTareas()
        print("===Marcar Tarea como Completada===")
        num = int(input("Ingrese el ID de la tarea a marcar como completada: "))
        MarcarTareaComoCompletada(num)
    elif opcion==3:
        VerTareas()
    elif opcion==4:
        VerTareas()
        print("===Eliminar Tarea===")
        num = int(input("Ingrese el ID de la tarea a eliminar: "))
        EliminarTarea(num)
    elif opcion == 5:
        conexion.close()
    else:
        print("Opcion Invalida")