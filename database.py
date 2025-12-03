import sqlite3

def conexion():
    return sqlite3.connect("Inventario.db")

def crear_tabla():
    conn=conexion()
    cur=conn.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS inventario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    marca TEXT,
                    modelo TEXT,
                    serial TEXT,
                    estado TEXT,
                    ram TEXT,
                    procesador TEXT,
                    almacenamiento TEXT,
                    sistema_operativo TEXT,
                    tiene_mouse TEXT,
                    tiene_teclado TEXT,
                    placa_sena TEXT UNIQUE,
                    fecha_registro TEXT
                    )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre TEXT, 
                    apellido TEXT, 
                    telefono TEXT, 
                    correo TEXT,
                    usuario TEXT UNIQUE,
                    clave TEXT
                )''')   
    cur.execute("SELECT * FROM usuarios WHERE usuario = usuario")
    if not cur.fetchone():
        cur.execute("INSERT INTO usuarios (nombre, apellido, telefono, correo, usuario, clave) VALUES (?, ?, ?, ?, ?, ?)", 
                    ("Wilfer", "Hernandez", "3108346231", "wilfer@gmail.com", "wilfer", "pass1234"))
    conn.commit()
    conn.close()
    
    
crear_tabla()
    
