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
        
        if tipo_entidad == 'libro':
            if operacion == 'insertar':
                nombre_libro = request.form['titulo']
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

        if tipo_entidad == 'Edicion':
            if operacion == 'insertar':
                ISBN = request.form['ISBN']
                año = request.form['año']
                idioma = request.form['idioma']
                mongo.db.Edicion.insert_one({'nombre': ISBN, 'año': año, 'idioma':idioma})
                flash('Edicion insertada correctamente', 'success')
            elif operacion == 'actualizar':
                ISBN = request.form['ISBN']
                ISBN_nuevo = request.form['ISBN_nuevo']
                año_nuevo = request.form['año_nuevo']
                idioma_nuevo = request.form['idioma_nuevo']
                mongo.db.Edicion.update_one({'ISBN': ISBN},{'$set': {'ISBN': ISBN_nuevo, 'año': año_nuevo, 'idioma': idioma_nuevo}})
                flash('Edicion actualizada correctamente', 'success')
            elif operacion == 'borrar':
                ISBN = request.form['ISBN']
                mongo.db.Edicion.delete_one({'ISBN': ISBN})
                flash('Edicion eliminada correctamente', 'success')
            
        elif tipo_entidad == 'copia':
            if operacion == 'insertar':
                    ISBN = request.form['ISBN']
                    numero_copia = request.form['numero_copia']
                    disponible = 'Si' if request.form.get('disponible', 'off') == 'on' else 'No'

                    mongo.db.Copias.insert_one({'ISBN': ISBN, 'numero': numero_copia, 'disponible': disponible})
                    flash('Copia insertada correctamente', 'success')
                    
            elif operacion == 'actualizar':
                    ISBN = request.form['ISBN']
                    ISBN_nuevo = request.form['ISBN_nuevo']
                    numero_copia = request.form['numero_copia']
                    numero_copia_nuevo = request.form['numero_copia_nuevo']
                    disponible = request.form.get('disponible', False) == 'on'

                    # Actualizar la disponibilidad de la copia en la colección Copias
                    mongo.db.Copias.update_one({'ISBN': ISBN, 'numero': numero_copia}, {'$set': {'disponible': disponible}})
                    flash('Copia actualizada correctamente', 'success')
            elif operacion == 'borrar':
                    ISBN = request.form['ISBN']
                    numero_copia = request.form['numero_copia']

                    # Eliminar la copia de la colección Copias
                    mongo.db.Copias.delete_one({'ISBN': ISBN, 'numero': numero_copia})
                    flash('Copia eliminada correctamente', 'success')
                    
                    
        elif tipo_entidad == 'usuario':
            if operacion == 'insertar':
                    RUT = request.form['RUT']
                    nombre = request.form['nombre']

                    mongo.db.Usuarios.insert_one({'RUT': RUT, 'nombre': nombre})
                    flash('Usuario insertado correctamente', 'success')
                    
            elif operacion == 'actualizar':
                    RUT = request.form['RUT']
                    nombre_nuevo = request.form['nombre_nuevo']

                    # Actualizar la disponibilidad de la copia en la colección Copias
                    mongo.db.Usuarios.update_one({'RUT': RUT}, {'$set': {'nombre': nombre_nuevo}})
                    flash('Usuario actualizado correctamente', 'success')
            elif operacion == 'borrar':
                    RUT = request.form['RUT']

                    # Eliminar la copia de la colección Copias
                    mongo.db.Usuarios.delete_one({'RUT': RUT})
                    flash('Usuario eliminado correctamente', 'success')

        elif tipo_entidad == 'prestamo':
            if operacion == 'insertar':
                RUT = request.form['RUT']
                ISBN = request.form['ISBN']
                fecha_prestamo = request.form['fecha_prestamo']
                fecha_devolucion = request.form['fecha_devolucion']

                mongo.db.Prestamos.insert_one({'RUT': RUT, 'ISBN': ISBN, 'fecha_prestamo': fecha_prestamo, 'fecha_devolucion': fecha_devolucion})
                flash('Préstamo insertado correctamente', 'success')
            elif operacion == 'actualizar':
                RUT = request.form['RUT']
                ISBN = request.form['ISBN']
                fecha_prestamo_nuevo = request.form['fecha_prestamo_nuevo']
                fecha_devolucion_nuevo = request.form['fecha_devolucion_nuevo']

                mongo.db.Prestamos.update_one({'RUT': RUT,'ISBN': ISBN}, {'$set': {'fecha_prestamo': fecha_prestamo_nuevo, 'fecha_devolucion': fecha_devolucion_nuevo}})
                flash('Préstamo actualizado correctamente', 'success')
            elif operacion == 'borrar':
                RUT = request.form['RUT']
                ISBN = request.form['ISBN']

                mongo.db.Prestamos.delete_one({'RUT': RUT, 'ISBN': ISBN})
                flash('Préstamo eliminado correctamente', 'success')
            
        elif tipo_entidad == 'autores':
            if operacion == 'insertar':
                nombre_autor = request.form['nombre']
                nombre_libro = request.form['titulo']

                mongo.db.Autores.insert_one({'nombre del autor': nombre_autor, 'nombre del libro': nombre_libro})
                flash('Autor y libro insertado correctamente', 'success')
            elif operacion == 'actualizar':
                nombre_autor = request.form['nombre']
                nombre_libro = request.form['titulo']
                nombre_nuevo_a = request.form['nombre_nuevo']
                nombre_nuevo = request.form['titulo_nuevo']

                mongo.db.Autores.update_one({'nombre del autor': nombre_autor,'nombre del libro': nombre_libro}, {'$set': {'nombre del autor': nombre_nuevo_a, 'nombre del libro': nombre_nuevo}})
                flash('Autor y libro actualizado correctamente', 'success')
            elif operacion == 'borrar':
                nombre_autor = request.form['nombre']
                nombre_libro = request.form['titulo']

                mongo.db.Autores.delete_one({'nombre del autor': nombre_autor, 'nombre del libro': nombre_libro})
                flash('Autor y libro eliminado correctamente', 'success')
                
        elif tipo_entidad == 'tiene':
            if operacion == 'insertar':
                nombre_libro = request.form['titulo']
                ISBN = request.form['ISBN']

                mongo.db.Tiene.insert_one({'nombre del libro': nombre_libro, 'ISBN': ISBN})
                flash('Libro e ISBN insertado correctamente', 'success')
            elif operacion == 'actualizar':
                nombre_libro = request.form['titulo']
                ISBN = request.form['ISBN']
                nombre_nuevo = request.form['titulo_nuevo']
                ISBN_nuevo = request.form['ISBN_nuevo']


                mongo.db.Tiene.update_one({'nombre del libro': nombre_libro, 'ISBN': ISBN}, {'$set': {'nombre del libro': nombre_nuevo, 'ISBN': ISBN_nuevo}})
                flash('Libro e ISBN  actualizado correctamente', 'success')
            elif operacion == 'borrar':
                nombre_libro = request.form['titulo']
                ISBN = request.form['ISBN']

                mongo.db.Tiene.delete_one({'nombre del libro': nombre_libro, 'ISBN': ISBN})
                flash('Libro e ISBN  eliminado correctamente', 'success')
                
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)