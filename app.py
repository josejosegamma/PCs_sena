from flask import Flask, render_template, request,redirect
from database import *

app=Flask(__name__)

crear_tabla()


@app.route('/')
def index():
    conn = conexion()
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventario") 
    computadores = cur.fetchall()
    conn.close()
    return render_template('index.html', computadores=computadores)



@app.route('/insertar', methods=['POST', 'GET'])
def insertar():
    if request.method == 'POST':
        marca=request.form['marca']
        modelo=request.form['modelo']
        serial=request.form['serial']
        estado=request.form['estado']
        ram=request.form['ram']
        procesador=request.form['procesador']
        almacenamiento=request.form['almacenamiento']
        sistema_operativo=request.form['sistema_operativo']
        tiene_mouse=request.form['tiene_mouse']
        tiene_teclado=request.form['tiene_teclado']
        placa_sena=request.form['placa_sena']
        fecha_registro=request.form['fecha_registro']
        
        conn = conexion()
        cur = conn.cursor()
        cur.execute("INSERT INTO inventario (marca, modelo, serial, estado, ram, procesador, almacenamiento, sistema_operativo, tiene_mouse, tiene_teclado, placa_sena, fecha_registro) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                       (marca, modelo, serial, estado, ram, procesador, almacenamiento, sistema_operativo, tiene_mouse, tiene_teclado, placa_sena, fecha_registro))
        conn.commit()
        conn.close()
        return redirect('/')
        
    return render_template('insertar.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == "POST":
        usuario = request.form["usuario"]
        clave = request.form["clave"]

        conn = conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND clave = ?", (usuario, clave))
        user = cursor.fetchone()

        if user:
            return redirect(f"/home?usuario={usuario}")
        else:
            error = "Usuario o contraseña incorrectos"

    return render_template('login.html', error=error)

@app.route("/home")
def home():
    usuario = request.args.get("usuario", "Invitado")
    conn = conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")  
    datos = cursor.fetchall()
    cursor.execute("SELECT * FROM inventario")  
    computadores = cursor.fetchall()
    conn.close()
    return render_template("home.html", usuarios=datos, computadores=computadores, usuario=usuario)
        
        
if __name__ == '__main__':
    app.run(debug=True)
