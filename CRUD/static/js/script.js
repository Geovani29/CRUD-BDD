document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('show-rut-btn').addEventListener('click', function(event) {
        event.preventDefault();
        document.getElementById('rut-form-container').classList.toggle('show');
    });

    // Ocultar el formulario al hacer clic nuevamente en el botón "Mostrar Listado de Libros Prestados Por Usuarios"
    document.getElementById('submit-rut-btn').addEventListener('click', function(event) {
        document.getElementById('rut-form-container').classList.remove('show');
    });

    // Manejar el envío del formulario
    document.getElementById('rut-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var rutValue = document.getElementById('RUT_input').value;
        window.location.href = "/resultados2?RUT=" + rutValue;
    });
});




        function mostrarCampos() {
            var tipoEntidad = document.getElementById('tipo_entidad').value;
            var operacion = document.getElementById('operacion').value;
    
            // Ocultar todos los campos
            document.querySelectorAll('.fields').forEach(function(field) {
                field.style.display = 'none';
            });
    
            // Mostrar los campos correspondientes según la operación y el tipo de entidad
            if (tipoEntidad === 'libro') {
                if (operacion === 'insertar' || operacion === 'borrar' || operacion === 'actualizar') {
                    document.getElementById('titulo_fields').style.display = 'block';
                    if (operacion === 'actualizar') {
                        document.getElementById('titulo_nuevo_fields').style.display = 'block';
                    }
                }
            } else if (tipoEntidad === 'edicion') {
                if (operacion === 'insertar' || operacion === 'actualizar') {
                    document.getElementById('ISBN_fields').style.display = 'block';
                    document.getElementById('año_fields').style.display = 'block';
                    document.getElementById('idioma_fields').style.display = 'block';
                    if (operacion === 'actualizar') {
                        document.getElementById('ISBN_nuevo_fields').style.display = 'block';
                        document.getElementById('año_nuevo_fields').style.display = 'block';
                        document.getElementById('idioma_nuevo_fields').style.display = 'block';
                    }
                }else if (operacion === 'borrar') {
                    document.getElementById('ISBN_fields').style.display = 'block';
                }
            } else if (tipoEntidad === 'copia') {
                if (operacion === 'insertar') {
                    document.getElementById('ISBN_fields').style.display = 'block';
                    document.getElementById('numero_copia_fields').style.display = 'block';
                    document.getElementById('disponible_fields').style.display = 'block';
                    
                }else if (operacion === 'actualizar') {
                    document.getElementById('ISBN_fields').style.display = 'block';
                    document.getElementById('numero_copia_fields').style.display = 'block';
                    document.getElementById('disponible_nuevo_fields').style.display = 'block';
                }else if (operacion === 'borrar') {
                    document.getElementById('ISBN_fields').style.display = 'block';
                    document.getElementById('numero_copia_fields').style.display = 'block';
                }
            } else if (tipoEntidad === 'usuario') {
                if (operacion === 'insertar' || operacion === 'borrar' || operacion === 'actualizar') {
                    document.getElementById('RUT').style.display = 'block';
                    document.getElementById('nombre_fields').style.display = 'block';
                    if (operacion === 'actualizar') {
                        document.getElementById('nombre_nuevo_fields').style.display = 'block';
                    }
                }
            } else if (tipoEntidad === 'prestamo') {
                if (operacion === 'insertar') {
                    document.getElementById('RUT').style.display = 'block';
                    document.getElementById('ISBN_fields').style.display = 'block';
                    document.getElementById('numero_copia_fields').style.display = 'block';
                    document.getElementById('fecha_prestamo_fields').style.display = 'block';
                    document.getElementById('fecha_devolucion_fields').style.display = 'block';
                } else if (operacion === 'actualizar') {
                    document.getElementById('RUT').style.display = 'block';
                    document.getElementById('ISBN_fields').style.display = 'block';
                    document.getElementById('numero_copia_nuevo_fields').style.display = 'block';
                    document.getElementById('fecha_prestamo_nuevo_fields').style.display = 'block';
                    document.getElementById('fecha_devolucion_nuevo_fields').style.display = 'block';
                }else if (operacion === 'borrar') {
                    document.getElementById('RUT').style.display = 'block';
                    document.getElementById('ISBN_fields').style.display = 'block';
                    document.getElementById('numero_copia_fields').style.display = 'block';
                }
                
            } else if (tipoEntidad === 'autores') {
                if (operacion === 'insertar' || operacion === 'borrar' || operacion === 'actualizar') {
                    document.getElementById('nombre_fields').style.display = 'block';
                    document.getElementById('titulo_fields').style.display = 'block';
                    if (operacion === 'actualizar') {
                        document.getElementById('nombre_nuevo_fields').style.display = 'block';
                        document.getElementById('titulo_nuevo_fields').style.display = 'block';
                    }
                }
            } else if (tipoEntidad === 'tiene') {
                    if (operacion === 'insertar' || operacion === 'borrar' || operacion === 'actualizar') {
                        document.getElementById('titulo_fields').style.display = 'block';
                        document.getElementById('ISBN_fields').style.display = 'block';
                        if (operacion === 'actualizar') {
                            document.getElementById('titulo_nuevo_fields').style.display = 'block';
                            document.getElementById('ISBN_nuevo_fields').style.display = 'block';
                        }
                    }
                                       
            } else {
                // Si no es una entidad específica, mostrar solo los campos de nombre
                document.getElementById('nombre_fields').style.display = 'block';
                if (operacion === 'actualizar') {
                    document.getElementById('nombre_nuevo_fields').style.display = 'block';
                }
            }
    
            // Mostrar campos de fecha solo cuando la entidad seleccionada sea "prestamo"
            if (tipoEntidad !== 'prestamo') {
                document.getElementById('fecha_prestamo_fields').style.display = 'none';
                document.getElementById('fecha_devolucion_fields').style.display = 'none';
                document.getElementById('fecha_prestamo_nuevo_fields').style.display = 'none';
                document.getElementById('fecha_devolucion_nuevo_fields').style.display = 'none';
            }
        }

        function resetForm() {
            document.querySelectorAll('.fields').forEach(function(field) {
                field.style.display = 'none';
            });

            document.getElementById('RUT').style.display = 'none';
            document.getElementById('nombre_nuevo_fields').style.display = 'none';
            document.getElementById('titulo_nuevo_fields').style.display = 'none';
            document.getElementById('ISBN_nuevo_fields').style.display = 'none';
            document.getElementById('año_nuevo_fields').style.display = 'none';
            document.getElementById('idioma_nuevo_fields').style.display = 'none';
            document.getElementById('numero_copia_nuevo_fields').style.display = 'none';
            document.getElementById('disponible_nuevo_fields').style.display = 'none';
            document.getElementById('fecha_prestamo_nuevo_fields').style.display = 'none';
            document.getElementById('fecha_devolucion_nuevo_fields').style.display = 'none';
            document.getElementById('tipo_entidad').selectedIndex = 0;
            document.getElementById('operacion').selectedIndex = 0;
        }
    
        // Mostrar campos al cargar la página si es necesario
        window.onload = function() {
            var tipoEntidadGuardada = localStorage.getItem('tipo_entidad');
            var operacionGuardada = localStorage.getItem('operacion');

            if (tipoEntidadGuardada && operacionGuardada) {
                document.getElementById('tipo_entidad').value = tipoEntidadGuardada;
                document.getElementById('operacion').value = operacionGuardada;
                mostrarCampos();
            }
        };
    
        // Recordar la selección de la entidad después de enviar el formulario
        document.getElementById('formulario').addEventListener('submit', function() {
            var tipoEntidad = document.getElementById('tipo_entidad').value;
            localStorage.setItem('tipo_entidad', tipoEntidad);

            // Guardar también la operación seleccionada
            var operacion = document.getElementById('operacion').value;
            localStorage.setItem('operacion', operacion);
        });
        // Establecer la entidad seleccionada al cargar la página nuevamente
        var tipoEntidadGuardada = localStorage.getItem('tipo_entidad');
        if (tipoEntidadGuardada) {
            document.getElementById('tipo_entidad').value = tipoEntidadGuardada;
            mostrarCampos();
        }