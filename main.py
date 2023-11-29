from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def menu_principal():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        edad = int(request.form.get('edad', 0))
        cantidad_tarros = int(request.form.get('tarros', 0))


        total_sin_descuento = cantidad_tarros * 9000


        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0


        total_con_descuento = total_sin_descuento * (1 - descuento)

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento': descuento,
            'total_con_descuento': total_con_descuento
        }

    return render_template('ejercicio1.html', resultado=resultado)


usuarios_registrados = {
    'juan': 'admin',
    'pepe': 'user'
}

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None

    if request.method == 'POST':
        usuario = request.form.get('usuario', '')
        contrasena = request.form.get('contrasena', '')


        if usuario in usuarios_registrados and usuarios_registrados[usuario] == contrasena:
            mensaje = f"Bienvenido {'administrador' if usuario == 'juan' else 'usuario'} {usuario}"

        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)