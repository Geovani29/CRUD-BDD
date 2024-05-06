from flask import Flask, render_template, request, flash
from flask_pymongo import PyMongo
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/biblioteca'  
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gestionar_datos', methods=['POST'])
def gestionar_datos():
    if request.method == 'POST':
        tipo_entidad = request.form['tipo_entidad']
        operacion = request.form['operacion']

        if tipo_entidad == 'autor':
            if operacion == 'insertar':
                nombre = request.form['nombre']
                if not nombre:
                    flash('Nombre de autor es requerido', 'error')
                    return render_template('index.html')
                if not re.match(r'^[a-zA-Z\s]+$', nombre):
                    flash('solo puede contener letras y espacios', 'error')
                    return render_template('index.html')
                # Verificar si el nombre de autor ya existe
                if mongo.db.Autor.find_one({'nombre': nombre}):
                    flash('Nombre de autor duplicado.', 'error')
                    return render_template('index.html')
                else:
                    mongo.db.Autor.insert_one({'nombre': nombre})
                    flash('Autor insertado correctamente', 'success')
            elif operacion == 'actualizar':
                nombre = request.form['nombre']
                nombre_nuevo = request.form['nombre_nuevo']
                if not all([nombre, nombre_nuevo]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                if not re.match(r'^[a-zA-Z\s]+$', nombre):
                    flash('Autor solo puede contener letras y espacios', 'error')
                    return render_template('index.html')
                if not mongo.db.Autor.find_one({'nombre': nombre}):
                    flash('Ese autor no existe', 'error')
                    return render_template('index.html')
                if mongo.db.Autor.find_one({'nombre': nombre_nuevo}):
                    flash('Nombre de autor duplicado.', 'error')
                    return render_template('index.html')
                mongo.db.Autor.update_one({'nombre': nombre}, {'$set': {'nombre': nombre_nuevo}})
                flash('Autor actualizado correctamente', 'success')
                
                
            elif operacion == 'borrar':
                nombre = request.form['nombre']
                if not request.form.get('nombre'):
                    flash('Nombre de autor es requerido', 'error')
                    return render_template('index.html')
                if not re.match(r'^[a-zA-Z\s]+$', nombre):
                    flash('Autor solo puede contener letras y espacios', 'error')
                    return render_template('index.html')
                if not mongo.db.Autor.find_one({'nombre': request.form['nombre']}):
                    flash('Ese autor no existe', 'error')
                    return render_template('index.html')
                mongo.db.Autor.delete_one({'nombre': nombre})
                flash('Autor eliminado correctamente', 'success')
            tipo_entidad = request.form['tipo_entidad']
            operacion = request.form['operacion']
        elif tipo_entidad == 'libro':
            if operacion == 'insertar':
                nombre_libro = request.form['titulo']
                if not nombre_libro:
                    flash('Titulo de libro es requerido', 'error')
                    return render_template('index.html')
                if mongo.db.Libros.find_one({'titulo': nombre_libro}):
                    flash('Titulo de libro duplicado.', 'error')
                    return render_template('index.html')
                else:
                    mongo.db.Libros.insert_one({'titulo': nombre_libro})
                    flash('libro insertado correctamente', 'success')
            elif operacion == 'actualizar':
                nombre_libro = request.form['titulo']
                nombre_nuevo = request.form['titulo_nuevo']
                if not all([nombre_libro, nombre_nuevo]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                if not mongo.db.Libros.find_one({'titulo': nombre_libro}):
                    flash('Ese libro no existe', 'error')
                    return render_template('index.html')
                if mongo.db.Libros.find_one({'titulo': nombre_nuevo}): 
                    flash('Titulo de libro duplicado.', 'error')
                    return render_template('index.html')
                mongo.db.Libros.update_one({'titulo': nombre_libro}, {'$set': {'titulo': nombre_nuevo}})
                flash('libro actualizado correctamente', 'success')
            elif operacion == 'borrar':
                if not request.form.get('titulo'):
                    flash('Titulo de libro es requerido', 'error')
                    return render_template('index.html')
                if not mongo.db.Libros.find_one({'titulo': request.form['titulo']}):
                    flash('Ese libro no existe', 'error')
                    return render_template('index.html')
                nombre_libro = request.form['titulo']
                mongo.db.Libros.delete_one({'titulo': nombre_libro})
                flash('libro eliminado correctamente', 'success')

        elif tipo_entidad == 'edicion':  # Corregir el valor aquí
            if operacion == 'insertar':
                isbn = request.form['ISBN'] 
                año = request.form['año']  
                idioma = request.form['idioma'] 
                if not all([isbn, año, idioma]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                if not re.match(r'^[0-9]+$', año):
                    flash('Año debe ser un número', 'error')
                    return render_template('index.html')
                if not re.match(r'^[a-zA-Z\s]+$', idioma):
                    flash('Idioma solo puede contener letras y espacios', 'error')
                    return render_template('index.html')
                if mongo.db.Ediciones.find_one({'ISBN': isbn}):
                    flash('ISBN de edición duplicado.', 'error')
                    return render_template('index.html')
                else: 
                    mongo.db.Ediciones.insert_one({'ISBN': isbn, 'año': año, 'idioma': idioma})
                    flash('Edición insertada correctamente', 'success')
            elif operacion == 'actualizar':
                isbn = request.form['ISBN']  
                isbn_nuevo = request.form['ISBN_nuevo']  
                año_nuevo = request.form['año_nuevo']  
                idioma_nuevo = request.form['idioma_nuevo']
                if not all([isbn, isbn_nuevo, año_nuevo, idioma_nuevo]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                if not re.match(r'^[0-9]+$', año_nuevo):
                    flash('Año debe ser un número', 'error')
                    return render_template('index.html')
                if not re.match(r'^[a-zA-Z\s]+$', idioma_nuevo):
                    flash('Idioma solo puede contener letras y espacios', 'error')
                    return render_template('index.html')
                if not mongo.db.Ediciones.find_one({'ISBN': isbn}):
                    flash('Ese ISBN no existe', 'error')
                    return render_template('index.html')
                if mongo.db.Ediciones.find_one({'ISBN': isbn_nuevo}):
                    flash('ISBN de edición duplicado.', 'error')
                    return render_template('index.html')
                mongo.db.Ediciones.update_one({'ISBN': isbn}, {'$set': {'idioma': idioma_nuevo}})
                flash('Edición actualizada correctamente', 'success')
            elif operacion == 'borrar': 
                isbn = request.form['ISBN']
                if not isbn:
                    flash('ISBN es requerido', 'error')
                    return render_template('index.html')
                if not mongo.db.Ediciones.find_one({'ISBN': isbn }): 
                    flash('Ese ISBN no existe', 'error')
                    return render_template('index.html')
                mongo.db.Ediciones.delete_one({'ISBN': isbn})
                flash('Edición eliminada correctamente', 'success')
            
        elif tipo_entidad == 'copia':
            if operacion == 'insertar':
                    ISBN = request.form['ISBN']
                    numero_copia = request.form['numero_copia']
                    disponible = 'Si' if request.form.get('disponible', 'off') == 'on' else 'No'
                    if not all([ISBN, numero_copia]):
                        flash('Todos los campos son requeridos', 'error')
                        return render_template('index.html')                   
                    if not mongo.db.Ediciones.find_one({'ISBN': ISBN}):
                        flash('Ese ISBN no existe', 'error')
                        return render_template('index.html')                   
                    if mongo.db.Copias.find_one({'ISBN': ISBN, 'numero': numero_copia}):
                        flash('Esa copia ya existe', 'error')
                        return render_template('index.html')
                    if not re.match(r'^[0-9]+$', numero_copia):
                        flash('Número de copia debe ser un número', 'error')
                        return render_template('index.html')
                    mongo.db.Copias.insert_one({'ISBN': ISBN, 'numero': numero_copia, 'disponible': disponible})
                    flash('Copia insertada correctamente', 'success')
                    
            elif operacion == 'actualizar':
                    ISBN = request.form['ISBN']
                    numero_copia = request.form['numero_copia']
                    disponible_nuevo  = 'Si' if request.form.get('disponible_nuevo', 'off') == 'on' else 'No'

                    if not all([ISBN, numero_copia]):
                        flash('ISBN y numero de copia son requeridos', 'error')
                        return render_template('index.html')
                    if not re.match(r'^[0-9]+$', numero_copia): 
                        flash('Número de copia debe ser un número', 'error')
                        return render_template('index.html')
                    
                    if not mongo.db.Copias.find_one({'ISBN': ISBN , 'numero': numero_copia}):
                        flash('Esa copia no existe', 'error')
                        return render_template('index.html')

                    # Actualizar la disponibilidad de la copia en la colección Copias
                    mongo.db.Copias.update_one({'ISBN': ISBN, 'numero': numero_copia}, {'$set': {'disponible': disponible_nuevo}})
                    flash('Copia actualizada correctamente', 'success')
            elif operacion == 'borrar':
                    ISBN = request.form['ISBN']
                    numero_copia = request.form['numero_copia']

                    if not all([ISBN, numero_copia]):
                        flash('Todos los campos son requeridos', 'error')
                        return render_template('index.html')
                    if not mongo.db.Copias.find_one({'ISBN ': ISBN, 'numero': numero_copia}): 
                        flash('Esa copia no existe', 'error')
                        return render_template('index.html')
                    if mongo.db.Prestamos.find_one({'ISBN': ISBN, 'numero_copia': numero_copia}):
                        flash('No se puede eliminar la copia porque tiene préstamos asociados', 'error')
                        return render_template('index.html')
                    # Eliminar la copia de la colección Copias
                    mongo.db.Copias.delete_one({'ISBN': ISBN, 'numero': numero_copia})
                    flash('Copia eliminada correctamente', 'success')
                    
                    
        elif tipo_entidad == 'usuario':
            if operacion == 'insertar':
                    RUT = request.form['RUT']
                    nombre = request.form['nombre']

                    if not all([RUT, nombre]):
                        flash('Todos los campos son requeridos', 'error')
                        return render_template('index.html')
                    if mongo.db.Usuarios.find_one({'RUT': RUT}): 
                        flash('Ese RUT ya existe', 'error')
                        return render_template('index.html')
                    if not re.match(r'^[a-zA-Z\s]+$', nombre):
                        flash('Nombre solo puede contener letras y espacios', 'error')
                        return render_template('index.html')

                    mongo.db.Usuarios.insert_one({'RUT': RUT, 'nombre': nombre})
                    flash('Usuario insertado correctamente', 'success')
                    
            elif operacion == 'actualizar':
                    RUT = request.form['RUT']
                    nombre_nuevo = request.form['nombre_nuevo']

                    if not all([RUT, nombre_nuevo]):
                        flash('Todos los campos son requeridos', 'error')
                        return render_template('index.html')    
                    if not mongo.db.Usuarios.find_one({'RUT': RUT}): 
                        flash('Ese RUT no existe', 'error')
                        return render_template('index.html')
                    if not re.match(r'^[a-zA-Z\s]+$', nombre_nuevo):
                        flash('Nombre solo puede contener letras y espacios', 'error')
                        return render_template('index.html')
                    if mongo.db.Prestamos.find_one({'RUT': RUT}):
                        flash('No se puede actualizar el usuario porque tiene préstamos asociados', 'error')
                        return render_template('index.html')
                    # Actualizar la disponibilidad de la copia en la colección Copias
                    mongo.db.Usuarios.update_one({'RUT': RUT}, {'$set': {'nombre': nombre_nuevo}})
                    flash('Usuario actualizado correctamente', 'success')
            elif operacion == 'borrar':
                    RUT = request.form['RUT']

                    if not RUT:
                        flash('Todos los campos son requeridos', 'error')
                        return render_template('index.html')

                    if not mongo.db.Usuarios.find_one({'RUT': RUT}): 
                        flash('Ese RUT no existe', 'error')
                        return render_template('index.html')

                    # Eliminar la copia de la colección Copias
                    mongo.db.Usuarios.delete_one({'RUT': RUT})
                    flash('Usuario eliminado correctamente', 'success')

        elif tipo_entidad == 'prestamo':
            if operacion == 'insertar':
                RUT = request.form['RUT']
                ISBN = request.form['ISBN']
                numero_copia = request.form['numero_copia']
                fecha_prestamo = request.form['fecha_prestamo']
                fecha_devolucion = request.form['fecha_devolucion']

                if not all([RUT, ISBN, numero_copia, fecha_prestamo, fecha_devolucion]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                if not re.match(r'^[0-9]+$', numero_copia):
                    flash('Número de copia debe ser un número', 'error')
                    return render_template('index.html')
                if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', fecha_prestamo):
                    flash('Formato de fecha de préstamo incorrecto', 'error')
                    return render_template('index.html')
                if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', fecha_devolucion):
                    flash('Formato de fecha de devolución incorrecto', 'error')
                    return render_template('index.html')               
                if not mongo.db.Usuarios.find_one({'RUT': RUT}):
                    flash('Ese RUT no existe', 'error')
                    return render_template('index.html')           
                if not mongo.db.Copias.find_one({'ISBN': ISBN, 'numero': numero_copia}): 
                    flash('Esa copia no existe', 'error')
                    return render_template('index.html')
                
                copia_existente = mongo.db.Copias.find_one({'ISBN': ISBN, 'numero': numero_copia})
                if not copia_existente:
                    flash('Esa copia no existe', 'error')
                    return render_template('index.html')
                
                if copia_existente['disponible'] == 'No':
                    flash('Esa copia no está disponible', 'error')
                    return render_template('index.html')
                
                if fecha_prestamo > fecha_devolucion:
                    flash('La fecha de préstamo debe ser menor o igual a la fecha de devolución', 'error')
                    return render_template('index.html')
                
                if mongo.db.Prestamos.find_one({'RUT': RUT, 'ISBN': ISBN, 'numero_copia': numero_copia}):
                    flash('Ese préstamo ya existe', 'error')
                    return render_template('index.html')

                mongo.db.Prestamos.insert_one({'RUT': RUT, 'ISBN': ISBN, 'numero_copia': numero_copia, 'fecha_prestamo': fecha_prestamo, 'fecha_devolucion': fecha_devolucion})
                flash('Préstamo insertado correctamente', 'success')
            elif operacion == 'actualizar':
                RUT = request.form['RUT']
                ISBN = request.form['ISBN']
                numero_copia_nuevo= request.form['numero_copia_nuevo']
                fecha_prestamo_nuevo = request.form['fecha_prestamo_nuevo']
                fecha_devolucion_nuevo = request.form['fecha_devolucion_nuevo']

                if not all([RUT, ISBN, numero_copia_nuevo, fecha_prestamo_nuevo, fecha_devolucion_nuevo]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                if not re.match(r'^[0-9]+$', numero_copia_nuevo):
                    flash('Número de copia debe ser un número', 'error')
                    return render_template('index.html')
                if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', fecha_prestamo_nuevo):
                    flash('Formato de fecha de préstamo incorrecto', 'error')
                    return render_template('index.html')
                if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', fecha_devolucion_nuevo):
                    flash('Formato de fecha de devolución incorrecto', 'error')
                    return render_template('index.html')
                
                if not mongo.db.Prestamos.find_one({'RUT': RUT, 'ISBN': ISBN, 'numero_copia': numero_copia_nuevo}):
                    flash('Ese préstamo no existe', 'error')
                    return render_template('index.html')
                
                if fecha_prestamo_nuevo > fecha_devolucion_nuevo:
                    flash('La fecha de préstamo debe ser menor o igual a la fecha de devolución', 'error')
                    return render_template('index.html')

                mongo.db.Prestamos.update_one({'RUT': RUT,'ISBN': ISBN}, {'$set': {'numero_copia':numero_copia_nuevo,'fecha_prestamo': fecha_prestamo_nuevo, 'fecha_devolucion': fecha_devolucion_nuevo}})
                flash('Préstamo actualizado correctamente', 'success')
            elif operacion == 'borrar':
                RUT = request.form['RUT']
                ISBN = request.form['ISBN']
                numero_copia = request.form['numero_copia']

                if not all([RUT, ISBN, numero_copia]):  
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                if not re.match(r'^[0-9]+$', numero_copia):
                    flash('Número de copia debe ser un número', 'error')
                    return render_template('index.html')

                if not mongo.db.Prestamos.find_one({'RUT': RUT, 'ISBN': ISBN, 'numero_copia': numero_copia}):
                    flash('Ese préstamo no existe', 'error')
                    return render_template('index.html')

                mongo.db.Prestamos.delete_one({'RUT': RUT, 'ISBN': ISBN, 'numero_copia': numero_copia})
                flash('Préstamo eliminado correctamente', 'success')
            
        elif tipo_entidad == 'autores':
            if operacion == 'insertar':
                nombre_autor = request.form['nombre']
                nombre_libro = request.form['titulo']

                if not all([nombre_autor, nombre_libro]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                if not re.match(r'^[a-zA-Z\s]+$', nombre_autor):
                    flash('Nombre de autor solo puede contener letras y espacios', 'error')
                    return render_template('index.html')
                if not mongo.db.Autor.find_one({'nombre': nombre_autor}):
                    flash('Autor no existe', 'error')
                    return render_template('index.html')
                if not mongo.db.Libros.find_one({'titulo': nombre_libro}):
                    flash('Libro no existe', 'error')
                    return render_template('index.html')
                if mongo.db.Autores.find_one({'nombre del autor': nombre_autor, 'nombre del libro': nombre_libro}):
                    flash('Ese autor y libro ya existe', 'error')
                    return render_template('index.html')
                mongo.db.Autores.insert_one({'nombre del autor': nombre_autor, 'nombre del libro': nombre_libro})
                flash('Autor y libro insertado correctamente', 'success')
            elif operacion == 'actualizar':
                nombre_autor = request.form['nombre']
                nombre_libro = request.form['titulo']
                nombre_nuevo_a = request.form['nombre_nuevo']
                nombre_nuevo = request.form['titulo_nuevo']

                if not all([nombre_autor, nombre_libro, nombre_nuevo_a, nombre_nuevo]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                if not re.match(r'^[a-zA-Z\s]+$', nombre_autor):
                    flash('Nombre de autor solo puede contener letras y espacios', 'error')
                    return render_template('index.html')
                if not mongo.db.Autores.find_one({'nombre del autor': nombre_autor, 'nombre del libro': nombre_libro}):
                    flash('Ese autor y libro no existe', 'error')
                    return render_template('index.html')
                if mongo.db.Autores.find_one({'nombre del autor': nombre_nuevo_a, 'nombre del libro': nombre_nuevo}): 
                    flash('Ese autor y libro ya existe', 'error')
                    return render_template('index.html')
                mongo.db.Autores.update_one({'nombre del autor': nombre_autor,'nombre del libro': nombre_libro}, {'$set': {'nombre del autor': nombre_nuevo_a, 'nombre del libro': nombre_nuevo}})
                flash('Autor y libro actualizado correctamente', 'success')
            elif operacion == 'borrar':
                nombre_autor = request.form['nombre']
                nombre_libro = request.form['titulo']

                if not all([nombre_autor, nombre_libro]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                if not re.match(r'^[a-zA-Z\s]+$', nombre_autor):
                    flash('Autor solo puede contener letras y espacios', 'error')
                    return render_template('index.html')
                if not mongo.db.Autores.find_one({'nombre del autor': nombre_autor, 'nombre del libro': nombre_libro}): 
                    flash('Ese autor y libro no existe', 'error')
                    return render_template('index.html')

                mongo.db.Autores.delete_one({'nombre del autor': nombre_autor, 'nombre del libro': nombre_libro})
                flash('Autor y libro eliminado correctamente', 'success')
                
        elif tipo_entidad == 'tiene':
            if operacion == 'insertar':
                nombre_libro = request.form['titulo']
                ISBN = request.form['ISBN']

                if not all([nombre_libro, ISBN]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')

                if not mongo.db.Libros.find_one({'titulo': nombre_libro}):
                    flash('Ese libro no existe', 'error')
                    return render_template('index.html')

                if not mongo.db.Ediciones.find_one({'ISBN': ISBN}):
                    flash('Ese ISBN no existe', 'error')
                    return render_template('index.html')
                
                if mongo.db.Tiene.find_one({'nombre del libro': nombre_libro, 'ISBN': ISBN}): 
                    flash('Ese libro e ISBN ya existe', 'error')
                    return render_template('index.html')
                
                mongo.db.Tiene.insert_one({'nombre del libro': nombre_libro, 'ISBN': ISBN})
                flash('Libro e ISBN insertado correctamente', 'success')
            elif operacion == 'actualizar':
                nombre_libro = request.form['titulo']
                ISBN = request.form['ISBN']
                nombre_nuevo = request.form['titulo_nuevo']
                ISBN_nuevo = request.form['ISBN_nuevo']
                if not all([nombre_libro, ISBN, nombre_nuevo, ISBN_nuevo]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                if not mongo.db.Libros.find_one({'titulo': nombre_libro}):
                    flash('Ese libro no existe', 'error')
                    return render_template('index.html')
                if not mongo.db.Ediciones.find_one({'ISBN': ISBN}):
                    flash('Ese ISBN no existe', 'error')
                    return render_template('index.html')               
                if mongo.db.Tiene.find_one({'nombre del libro': nombre_nuevo, 'ISBN': ISBN_nuevo}):
                    flash('Ese libro e ISBN ya existe', 'error')
                    return render_template('index.html')
                mongo.db.Tiene.update_one({'nombre del libro': nombre_libro, 'ISBN': ISBN}, {'$set': {'nombre del libro': nombre_nuevo, 'ISBN': ISBN_nuevo}})
                flash('Libro e ISBN  actualizado correctamente', 'success')
            elif operacion == 'borrar':
                nombre_libro = request.form['titulo']
                ISBN = request.form['ISBN']

                if not all([nombre_libro, ISBN]):
                    flash('Todos los campos son requeridos', 'error')
                    return render_template('index.html')
                
                if not mongo.db.Libros.find_one({'titulo': nombre_libro}):
                    flash('Ese libro no existe', 'error')
                    return render_template('index.html')

                if not mongo.db.Ediciones.find_one({'ISBN': ISBN}):
                    flash('Ese ISBN no existe', 'error')
                    return render_template('index.html')    

                mongo.db.Tiene.delete_one({'nombre del libro': nombre_libro, 'ISBN': ISBN})
                flash('Libro e ISBN  eliminado correctamente', 'success')
                
    return render_template('index.html')

@app.route('/resultados', methods=['GET', 'POST'])
def mostrar_resultados():
    resultados = list(mongo.db.Autor.aggregate([
  {
    "$lookup": {
      "from": "Autores",
      "localField": "nombre",
      "foreignField": "nombre del autor",
      "as": "autor_info"
    }
  },
  {
    "$unwind": "$autor_info"
  },
  {
    "$lookup": {
      "from": "Libros",
      "localField": "autor_info.nombre del libro", 
      "foreignField": "titulo",
      "as": "libro_info"
    }
  },
  {
    "$unwind": "$libro_info"
  },
  {
    "$lookup": {
      "from": "Tiene",
      "localField": "libro_info.titulo",
      "foreignField": "nombre del libro",  
      "as": "tiene_info"
    }
  },
  {
    "$unwind": "$tiene_info"
  },
  {
    "$lookup": {
      "from": "Ediciones",
      "localField": "tiene_info.ISBN",
      "foreignField": "ISBN",
      "as": "edicion_info"
    }
  },
  {
    "$unwind": "$edicion_info"
  },
  {
    "$lookup": {
      "from": "Copias",
      "localField": "edicion_info.ISBN",
      "foreignField": "ISBN",
      "as": "copias_info"
    }
  },
  {
    "$unwind": "$copias_info"
  },
  {
    "$project": {
      "nombre_autor": "$nombre",
      "nombre_libro": "$libro_info.titulo",
      "ISBN": "$edicion_info.ISBN",
      "año": "$edicion_info.año",
      "idioma": "$edicion_info.idioma",
      "numero_copia": "$copias_info.numero"
    }
  }
]))


    return render_template('resultados.html', resultados=resultados)

@app.route('/resultados2', methods=['GET', 'POST'])
def resultados_rut():
    if request.method == 'POST':
        rut = request.form['RUT']
        if not rut:
            flash('RUT es requerido', 'error')
            return render_template('resultado2.html')
        if not mongo.db.Usuarios.find_one({'RUT': rut}):
            flash('Ese RUT no existe', 'error')
            return render_template('resultado2.html', rut=rut)
        resultados_rut = mongo.db.Usuarios.aggregate([
            {
                "$match": {
                    "RUT": rut
                }
            },
            {
                "$lookup": {
                    "from": "Prestamos",
                    "localField": "RUT",
                    "foreignField": "RUT",
                    "as": "prestamos"
                }
            },
            {
                "$unwind": "$prestamos"
            },
            {
                "$lookup": {
                    "from": "Tiene",
                    "localField": "prestamos.ISBN",
                    "foreignField": "ISBN",
                    "as": "tiene_info"
                }
            },
            {
                "$unwind": "$tiene_info"
            },
            {
                "$project": {
                    "_id": 0,
                    "nombre": 1,
                    "nombre_libro": "$tiene_info.nombre del libro",
                    "ISBN": "$prestamos.ISBN",
                    "numero_copia": "$prestamos.numero_copia",
                    "fecha_prestamo": "$prestamos.fecha_prestamo",
                    "fecha_devolucion": "$prestamos.fecha_devolucion"
                }
            }
        ])
        return render_template('resultado2.html', resultados=resultados_rut, rut=rut)
    else:
        # Si la solicitud es GET, simplemente renderiza la página resultados_rut.html sin resultados
        return render_template('resultado2.html')

@app.route('/TablaAutor', methods=['GET', 'POST'])
def Tabla_Autor():
    if request.method == 'POST':
        resultados_autor = mongo.db.Autor.find()
        return render_template('TablaAutor.html', resultados=resultados_autor)
    else:
        return render_template('TablaAutor.html')

@app.route('/TablaAutores', methods=['GET', 'POST'])
def Tabla_Autores():
    if request.method == 'POST':
        resultados_autores = mongo.db.Autores.find()
        return render_template('TablaAutores.html', resultados=resultados_autores)
    else:
        return render_template('TablaAutores.html')
    
@app.route('/TablaLibros', methods=['GET', 'POST'])
def Tabla_Libros():
    if request.method == 'POST':
        resultados_libro = mongo.db.Libros.find()
        return render_template('TablaLibros.html', resultados=resultados_libro)
    else:
        return render_template('TablaLibros.html')

@app.route('/TablaEdiciones', methods=['GET', 'POST'])
def Tabla_Ediciones():
    if request.method == 'POST':
        resultados_ediciones = mongo.db.Ediciones.find()
        return render_template('TablaEdiciones.html', resultados=resultados_ediciones)
    else:
        return render_template('TablaEdiciones.html')
    
@app.route('/TablaTiene', methods=['GET', 'POST'])
def Tabla_Tiene():
    if request.method == 'POST':
        resultados_Tiene = mongo.db.Tiene.find()
        return render_template('TablaTiene.html', resultados=resultados_Tiene)
    else:
        return render_template('TablaTiene.html')
    
@app.route('/TablaUsuarios', methods=['GET', 'POST'])
def Tabla_Usuarios():
    if request.method == 'POST':
        resultados_Usuarios = mongo.db.Usuarios.find()
        return render_template('TablaUsuarios.html', resultados=resultados_Usuarios)
    else:
        return render_template('TablaUsuarios.html')
    
@app.route('/TablaPrestamos', methods=['GET', 'POST'])
def Tabla_Prestamos():
    if request.method == 'POST':
        resultados_prestamos = mongo.db.Prestamos.find()
        return render_template('TablaPrestamos.html', resultados=resultados_prestamos)
    else:
        return render_template('TablaPrestamos.html')
    
@app.route('/TablaCopias', methods=['GET', 'POST'])
def Tabla_Copias():
    if request.method == 'POST':
        resultados_copias = mongo.db.Copias.find()
        return render_template('TablaCopias.html', resultados=resultados_copias)
    else:
        return render_template('TablaCopias.html')

if __name__ == '__main__':
    app.run(debug=True)