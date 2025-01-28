#Simulacion de una academia

# Crear, editar y eliminar

# FUNCIONES -------------------

def add_Student_List(nombre_estudiante, correo, cedula):
        
    estudianteList = []
    estudianteList.append(nombre_estudiante)
    estudianteList.append(correo)
    estudianteList.append(cedula)
    return estudianteList

def edit_Student_List(listaEstudiante: list, indice, valor):
    
    if indice < len(listaEstudiante):
        listaEstudiante[indice] = valor
    else:
        print("Indice esta fuera de rango")
        
    return listaEstudiante

def eliminar_Por_Indice_Estudiante(listaEstudiante: list, indice):
    
    if indice < len(listaEstudiante):
        listaEstudiante = listaEstudiante.pop(indice)
    else:
        print("Indice esta fuera de rango")
        
    return listaEstudiante
    
"""
Funcion para añadir una lista a una lista existente.
"""
def add_ListOfStudents(studentList: list, studentList2: list, index):
    
    if index < len(studentList):
        studentList = studentList.insert(index, studentList2)
    else:
        print("Indice esta fuera de rango")
    
    return studentList

def add_Values_ListStudents(studentList: list, studentList2: list):
    
    StudentList = studentList.extend(studentList2)
    
    return StudentList

# INPUTS ----------------------------------------------

student_name = input("Ingrese el nombre del estudiante: ")
email = input("Ingrese el correo del estudiante: ")
id_number = int(input("Ingrese el cedula del estudiante: "))

# LLAMADO DE FUNCIONES ----------------------

# Añadimos una lista con los valores del usuario
StudentList = add_Student_List(student_name, email, id_number)
print("\nLista de estudiantes:", StudentList, "\n")

"""index = int(input("Ingrese donde esta ubicado el valor a modificar: "))
valor = input("Ingrese el nuevo valor del estudiante: ")
edit_Student_List(StudentList, index, valor)
print("\nLista de estudiantes MODIFICADA:", StudentList, "\n")"""

"""index = int(input("Ingrese donde esta ubicado el valor a eliminar: "))
valor_eliminado = eliminar_Por_Indice_Estudiante(StudentList,index)
print("El valor eliminado es: " + valor_eliminado)
print("Lista de estudiantes ACTUALIZADA: ", StudentList)
"""

# Funcion para agregar lista a una lista existente
nombres = ['Juan', 'Maria', 'Manuel']
"""
index = int(input("Ingrese donde quiere insertar la lista: "))
add_ListOfStudents(StudentList,nombres, index)
print("\nLista de estudiantes insertada correctamente: ", StudentList, "\n")"""

# Funcion para agregar elementos de una lista a una lista
add_Values_ListStudents(StudentList, nombres)
print("\nValores de la lista agregados correctamente: ", StudentList, "\n")




#print(eliminar_Por_Indice_Estudiante(StudentList, 2))
#print(StudentList)