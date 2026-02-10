import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import sqlite3



# ------------------ BLOQUES 1–7 (SIN CAMBIOS) ------------------

def conectar_db():
    return sqlite3.connect("productos.db")


def crear_tabla():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            codigo TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            stock INTEGER NOT NULL
        )   
    """)
    conn.commit()
    conn.close()


def obtener_producto(codigo):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nombre, stock FROM productos WHERE codigo = ?",
        (codigo,)
    )
    producto = cursor.fetchone()
    conn.close()
    return producto

#obtiene todos los productos de la opcion 2
def obtener_todos_los_productos():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, nombre, stock FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos


def guardar_producto(codigo, nombre, stock):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO productos (codigo, nombre, stock)
        VALUES (?, ?, ?)
    """, (codigo, nombre, stock))
    conn.commit()
    conn.close()

#para la tabla de la opcion 2
def mostrar_tabla_productos():
    productos = obtener_todos_los_productos()

    ventana = tk.Toplevel(root)
    ventana.title("Consulta de productos")

    tabla = ttk.Treeview(
        ventana,
        columns=("codigo", "nombre", "stock"),
        show="headings"
    )

    tabla.heading("codigo", text="Código")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("stock", text="Stock")

    tabla.column("codigo", width=120)
    tabla.column("nombre", width=200)
    tabla.column("stock", width=80)

    for codigo, nombre, stock in productos:
        tabla.insert("", tk.END, values=(codigo, nombre, stock))

    tabla.pack(expand=True, fill="both")


def eliminar_producto(codigo):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
    conn.commit()
    conn.close()


crear_tabla()


# ------------------ INTERFAZ GRÁFICA ------------------

root = tk.Tk()
root.title("Bienvenido al programa")
root.geometry("420x300")


# -------- VENDER PRODUCTO --------
def vender_producto():
    codigo = simpledialog.askstring(
        "Vender producto",
        "Código del producto (o Enter vacío para volver al menú):"
    )

    if not codigo:
        return

    codigo = codigo.strip().upper()
    producto = obtener_producto(codigo)

    if not producto:
        messagebox.showerror("Error", "❌ Producto no registrado.")
        return

    nombre, stock = producto

    if stock <= 0:
        messagebox.showwarning(
            "Stock",
            f"⚠️ No es posible vender el producto '{nombre}', no hay STOCK."
        )
        return

    cantidad = simpledialog.askinteger(
        "Cantidad",
        "Cantidad a vender:"
    )

    if cantidad is None or cantidad <= 0:
        messagebox.showerror("Error", "❌ La cantidad debe ser mayor a 0.")
        return

    if cantidad > stock:
        messagebox.showerror(
            "Error",
            "  Stock icnsufiiente. No se realizó la venta."
        )
        return

    stock -= cantidad
    guardar_producto(codigo, nombre, stock)

    messagebox.showinfo(
        "Venta",
        f"✅ Venta registrada correctamente.\nStock restante: {stock}"
    )


# -------- CONSULTAR PRODUCTO --------
def consultar_producto():
    productos = obtener_todos_los_productos()

    ventana = tk.Toplevel(root)
    ventana.title("Consulta de productos")
    ventana.geometry("450x300")

    # ---------- ESTILO (BORDES + CELDAS) ----------
    style = ttk.Style()
    style.theme_use("default")

    style.configure(
        "Treeview",
        rowheight=25,
        borderwidth=1,
        relief="solid"
    )

    style.configure(
        "Treeview.Heading",
        borderwidth=1,
        relief="solid"
    )

    # ---------- TABLA ----------
    tabla = ttk.Treeview(
        ventana,
        columns=("codigo", "nombre", "stock"),
        show="headings"
    )

    tabla.heading("codigo", text="Código")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("stock", text="Stock")

    tabla.column("codigo", width=120, anchor="center")
    tabla.column("nombre", width=220, anchor="w")
    tabla.column("stock", width=80, anchor="center")

    # ---------- COLORES POR FILA ----------
    tabla.tag_configure("par", background="#f2f2f2")
    tabla.tag_configure("impar", background="#ffffff")

    for i, (codigo, nombre, stock) in enumerate(productos):
        tag = "par" if i % 2 == 0 else "impar"
        tabla.insert("", tk.END, values=(codigo, nombre, stock), tags=(tag,))

    tabla.pack(expand=True, fill="both")


# -------- AGREGAR / MODIFICAR --------
def agregar_modificar():
    codigo = simpledialog.askstring(
        "Agregar / Modificar",
        "Escribe el CÓDIGO existente o nuevo (presiona Enter una vez ingresado el codigo para continuar):"
    )

    if not codigo:
        return

    codigo = codigo.strip().upper()
    producto = obtener_producto(codigo)

    if producto:
        nombre, stock = producto
        if messagebox.askyesno("Producto", "  El producto ya existe.\n¿Deseas modificarlo?"):
            nombre = simpledialog.askstring("Nombre", "Nuevo nombre:", initialvalue=nombre)
            stock = simpledialog.askinteger("Stock", "Nuevo stock:", initialvalue=stock)

            if stock is not None and stock >= 0:
                guardar_producto(codigo, nombre, stock)
                messagebox.showinfo("OK", "✅ Producto actualizado correctamente.")
    else:
        nombre = simpledialog.askstring("Producto nuevo", "Nombre del producto:")
        stock = simpledialog.askinteger("Stock", "Stock:")

        if stock is not None and stock >= 0:
            guardar_producto(codigo, nombre, stock)
            messagebox.showinfo("OK", "✅ Producto agregado correctamente.")


# ------------------ BOTONES MENÚ ------------------

tk.Label(
    root,
    text="TECHMEDIUM\n----MENÚ----\n",
    font=("Arial", 12)
).pack(pady=10)

tk.Button(root, text="1. Vender producto", width=30, command=vender_producto).pack(pady=5)
tk.Button(root, text="2. Consultar productos", width=30, command=consultar_producto).pack(pady=5)
tk.Button(root, text="3. Agregar o modificar código/producto", width=30, command=agregar_modificar).pack(pady=5)
tk.Button(root, text="4. Salir del programa", width=30, command=root.quit).pack(pady=10)

root.mainloop()
