from flask import Flask, render_template, request, flash
from flask_pymongo import PyMongo

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
                nombre_autor = request.form['nombre']
                # Verificar si el nombre de autor ya existe
                if mongo.db.Autores.find_one({'nombre': nombre_autor}):
                    flash('Nombre de autor duplicado. Ingrese un nombre diferente', 'error')
                    return render_template('index.html')
                else:
                    mongo.db.Autores.insert_one({'nombre': nombre_autor})
                    flash('Autor insertado correctamente', 'success')
            elif operacion == 'actualizar':
                nombre_autor = request.form['nombre']
                nombre_nuevo = request.form['nombre_nuevo']
                mongo.db.Autores.update_one({'nombre': nombre_autor}, {'$set': {'nombre': nombre_nuevo}})
                flash('Autor actualizado correctamente', 'success')
            elif operacion == 'borrar':
                nombre_autor = request.form['nombre']
                mongo.db.Autores.delete_one({'nombre': nombre_autor})
                flash('Autor eliminado correctamente', 'success')
            tipo_entidad = request.form['tipo_entidad']
            operacion = request.form['operacion']
        
        elif tipo_entidad == 'libro':
            if operacion == 'insertar':
                nombre_libro = request.form['titulo']
                if mongo.db.Libros.find_one({'titulo': nombre_libro}):
                    flash('Titulo de libro duplicado. Ingrese un nombre diferente', 'error')
                    return render_template('index.html')
                else:
                    mongo.db.Libros.insert_one({'titulo': nombre_libro})
                    flash('libro insertado correctamente', 'success')
            elif operacion == 'actualizar':
                nombre_libro = request.form['titulo']
                nombre_nuevo = request.form['titulo_nuevo']
                mongo.db.Libros.update_one({'titulo': nombre_libro}, {'$set': {'titulo': nombre_nuevo}})
                flash('libro actualizado correctamente', 'success')
            elif operacion == 'borrar':
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
                if mongo.db.Ediciones.find_one({'ISBN': isbn}):
                    flash('ISBN de edición duplicado. Ingrese un ISBN diferente', 'error')
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
                mongo.db.Ediciones.update_one({'ISBN': isbn}, {'$set': {'ISBN': isbn_nuevo, 'año': año_nuevo, 'idioma': idioma_nuevo}})
                flash('Edición actualizada correctamente', 'success')
            elif operacion == 'borrar':
                isbn = request.form['ISBN']
                if not isbn:
                    flash('ISBN es requerido', 'error')
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

                    mongo.db.Copias.insert_one({'ISBN': ISBN, 'numero': numero_copia, 'disponible': disponible})
                    flash('Copia insertada correctamente', 'success')
                    
            elif operacion == 'actualizar':
                    ISBN = request.form['ISBN']
                    ISBN_nuevo = request.form['ISBN_nuevo']
                    numero_copia = request.form['numero_copia']
                    numero_copia_nuevo = request.form['numero_copia_nuevo']
                    disponible = request.form.get('disponible', False) == 'on'

                    if not all([ISBN, ISBN_nuevo, numero_copia, numero_copia_nuevo]):
                        flash('Todos los campos son requeridos', 'error')
                        return render_template('index.html')

                    # Actualizar la disponibilidad de la copia en la colección Copias
                    mongo.db.Copias.update_one({'ISBN': ISBN, 'numero': numero_copia}, {'$set': {'disponible': disponible}})
                    flash('Copia actualizada correctamente', 'success')
            elif operacion == 'borrar':
                    ISBN = request.form['ISBN']
                    numero_copia = request.form['numero_copia']

                    if not all([ISBN, numero_copia]):
                        flash('Todos los campos son requeridos', 'error')
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

                    mongo.db.Usuarios.insert_one({'RUT': RUT, 'nombre': nombre})
                    flash('Usuario insertado correctamente', 'success')
                    
            elif operacion == 'actualizar':
                    RUT = request.form['RUT']
                    nombre_nuevo = request.form['nombre_nuevo']

                    if not all([RUT, nombre_nuevo]):
                        flash('Todos los campos son requeridos', 'error')
                        return render_template('index.html')    

                    # Actualizar la disponibilidad de la copia en la colección Copias
                    mongo.db.Usuarios.update_one({'RUT': RUT}, {'$set': {'nombre': nombre_nuevo}})
                    flash('Usuario actualizado correctamente', 'success')
            elif operacion == 'borrar':
                    RUT = request.form['RUT']

                    if not RUT:
                        flash('Todos los campos son requeridos', 'error')
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

                mongo.db.Prestamos.update_one({'RUT': RUT,'ISBN': ISBN}, {'$set': {'numero_copia':numero_copia_nuevo,'fecha_prestamo': fecha_prestamo_nuevo, 'fecha_devolucion': fecha_devolucion_nuevo}})
                flash('Préstamo actualizado correctamente', 'success')
            elif operacion == 'borrar':
                RUT = request.form['RUT']
                ISBN = request.form['ISBN']
                numero_copia = request.form['numero_copia']

                if not all([RUT, ISBN, numero_copia]):  
                    flash('Todos los campos son requeridos', 'error')
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

                mongo.db.Autores.update_one({'nombre del autor': nombre_autor,'nombre del libro': nombre_libro}, {'$set': {'nombre del autor': nombre_nuevo_a, 'nombre del libro': nombre_nuevo}})
                flash('Autor y libro actualizado correctamente', 'success')
            elif operacion == 'borrar':
                nombre_autor = request.form['nombre']
                nombre_libro = request.form['titulo']

                if not all([nombre_autor, nombre_libro]):
                    flash('Todos los campos son requeridos', 'error')
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


                mongo.db.Tiene.update_one({'nombre del libro': nombre_libro, 'ISBN': ISBN}, {'$set': {'nombre del libro': nombre_nuevo, 'ISBN': ISBN_nuevo}})
                flash('Libro e ISBN  actualizado correctamente', 'success')
            elif operacion == 'borrar':
                nombre_libro = request.form['titulo']
                ISBN = request.form['ISBN']

                if not all([nombre_libro, ISBN]):
                    flash('Todos los campos son requeridos', 'error')
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


if __name__ == '__main__':
    app.run(debug=True)